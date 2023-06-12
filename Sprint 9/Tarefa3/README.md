# Tarefa 2:
### Processamento -  Camada Trusted

### Criando a camada Trusted para a carga histórica para o processamento do csv:
~~~python
import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler os dados do arquivo CSV
input_directory = args['S3_INPUT_PATH']
df = spark.read.format("csv").option("header", True).option("inferSchema", True).option("delimiter", "|").load(input_directory)

# Verificar o esquema do DataFrame
df.printSchema()

# Selecionar as colunas separadas para o DataFrame de saída
processed_data = df.select(
    col("id").alias("id"),
    col("tituloPincipal").alias("tituloPincipal"),
    col("tituloOriginal").alias("tituloOriginal"),
    col("anoLancamento").alias("anoLancamento"),
    col("tempoMinutos").alias("tempoMinutos"),
    col("genero").alias("genero"),
    col("notaMedia").alias("notaMedia"),
    col("numeroVotos").alias("numeroVotos"),
    col("generoArtista").alias("generoArtista"),
    col("personagem").alias("personagem"),
    col("nomeArtista").alias("nomeArtista"),
    col("anoNascimento").alias("anoNascimento"),
    col("anoFalecimento").alias("anoFalecimento"),
    col("profissao").alias("profissao"),
    col("titulosMaisConhecidos").alias("titulosMaisConhecidos")
)

# Definir o caminho de destino
target_directory = args['S3_TARGET_PATH']

# Escrever os dados no formato Parquet
processed_data.write.parquet(target_directory)

job.commit()
~~~

> O código em questão é um script em Python que utiliza a biblioteca AWS Glue e o Apache Spark para realizar a leitura de um arquivo CSV, transformar os dados selecionando algumas colunas específicas e gravar o resultado em um diretório de destino no formato Parquet.

# Output

![JOB 1](img/succeedjob1.png)


### Criando a camada Trusted para a carga de dados:
~~~python
import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa a sessão Spark e o Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Obtém o diretório de entrada e saída e cria uma pasta de destino com o nome de "tmbd"
input_directory = args['S3_INPUT_PATH']
target_directory = args['S3_TARGET_PATH']+'tmdb/'

# Lê os arquivos .JSON no diretório de entrada, os que possuam "new.json" no nome
input_data = spark.read.json(input_directory + "*new*.json")

# Seleciona as colunas do DataFrame de entrada
processed_data = input_data.select("tituloPrincipal", "tituloOriginal", "anoLancamento", "genero")

# Escreve os dados processados no formato Parquet no diretório
processed_data.write.parquet(target_directory)

job.commit()
~~~

> O código fornecido realiza a leitura de arquivos JSON no AWS Glue, seleciona algumas colunas específicas e grava os dados processados em um diretório de destino no formato Parquet.

# Output

![JOB 2](img/succeedjob2.png)

