import os
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand
from pyspark.sql.types import IntegerType


# Definindo o diretório e copiando o arquivo nomes_aleatorios.txt
data_dir = "diretorio/txt"
arquivo_nomes = "nomes_aleatorios.txt"
caminho_arquivo = os.path.join(data_dir, arquivo_nomes)
os.makedirs(data_dir, exist_ok=True)
shutil.copy(arquivo_nomes, caminho_arquivo)

# Importando as bibliotecas necessárias
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand
from pyspark.sql.types import IntegerType

# Definindo a Spark Session e o Spark Context
spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

# Lendo o arquivo nomes_aleatorios.txt e criando o DataFrame df_nomes
df_nomes = spark.read.text(caminho_arquivo)
df_nomes = df_nomes.withColumnRenamed("value", "Nomes")
df_nomes.show(5)

# Exibindo o Schema do DataFrame
df_nomes.printSchema()

# Renomeando a coluna para 'Nomes'
df_nomes = df_nomes.withColumnRenamed("value", "Nomes")
df_nomes.show(10)

# Adicionando a coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn("Escolaridade", when((rand() * 3).cast(IntegerType()) == 0, "Fundamental")
                                             .when((rand() * 3).cast(IntegerType()) == 1, "Medio")
                                             .otherwise("Superior"))

# Adicionando a coluna 'Pais' com valores aleatórios dos países da América do Sul
paises_am_sul = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Paraguai",
                 "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]
df_nomes = df_nomes.withColumn("Pais", when((rand() * len(paises_am_sul)).cast(IntegerType()) == 0, paises_am_sul[0])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 1, paises_am_sul[1])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 2, paises_am_sul[2])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 3, paises_am_sul[3])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 4, paises_am_sul[4])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 5, paises_am_sul[5])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 6, paises_am_sul[6])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 7, paises_am_sul[7])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 8, paises_am_sul[8])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 9, paises_am_sul[9])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 10, paises_am_sul[10])
                                         .when((rand() * len(paises_am_sul)).cast(IntegerType()) == 11, paises_am_sul[11])
                                         .otherwise(paises_am_sul[12]))

# Adicionando a coluna 'AnoNascimento' com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn("AnoNascimento", (rand() * (2010 - 1945) + 1945).cast(IntegerType()))

# Selecionando as pessoas que nasceram neste século
df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)
df_select.show(10)

# Registrando o DataFrame como uma tabela temporária
df_nomes.createOrReplaceTempView("pessoas")

# Executando a consulta SQL para selecionar as pessoas que nasceram neste século
df_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
df_sql.show(10)

# Contando o número de pessoas da geração Millennials usando DataFrame
count_millennials_df = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).count()
print("Número de pessoas da geração Millennials (usando DataFrame):", count_millennials_df)

# Contando o número de pessoas da geração Millennials usando Spark SQL
count_millennials_sql = spark.sql("SELECT COUNT(*) AS count_millennials FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]
print("Número de pessoas da geração Millennials (usando Spark SQL):", count_millennials_sql)

# Obtendo a quantidade de pessoas de cada país para uma das gerações
geracoes = [("Baby Boomers", 1944, 1964), ("Geração X", 1965, 1979),
            ("Millennials", 1980, 1994), ("Geração Z", 1995, 2015)]
df_geracoes_pais = spark.sql("""
    SELECT Pais, '{}' AS Geracao, COUNT(*) AS Quantidade
    FROM pessoas
    WHERE AnoNascimento BETWEEN {} AND {}
    GROUP BY Pais
    ORDER BY Pais, Geracao, Quantidade
""".format(geracoes[2][0], geracoes[2][1], geracoes[2][2]))
df_geracoes_pais.show()
