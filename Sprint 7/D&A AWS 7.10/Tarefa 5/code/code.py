import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# @params: [JOB_NAME]
args = getResolvedOptions(
    sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)

data_frame = df.toDF()

# Imprime o schema do dataframe gerado no passo anterior.
data_frame.printSchema()

# Aplica a transformação para converter os valores da coluna "nome" para maiúsculo
data_frame = data_frame.withColumn("nome", F.upper(F.col("nome")))
data_frame.show()

# Contagem de linhas
count = data_frame.count()
print('Contagem de linhas', count)

# Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
counts_df = data_frame.groupBy("ano", "sexo").count()
counts_df = counts_df.orderBy(F.desc("ano"))
counts_df.show()

# Apresentar o nome feminino/masculino com mais registros e em que ano ocorreu
count_df = data_frame.groupBy("nome", "sexo").agg(
    F.sum("total").alias("count"))
window = Window.partitionBy("sexo").orderBy(F.desc("count"))

nome_feminino_mais_registros = count_df.filter(count_df.sexo == "F").withColumn(
    "rank", F.rank().over(window)).filter(F.col("rank") == 1).select("nome", "count").first()
nome_feminino = nome_feminino_mais_registros["nome"]
print("Nome feminino com mais registros:", nome_feminino)

total_registros_feminino = nome_feminino_mais_registros["count"]
ano_ocorrencia_feminino = data_frame.filter((data_frame.sexo == "F") & (
    data_frame.nome == nome_feminino)).orderBy("ano").first()["ano"]
print("Total de registros femininos:", total_registros_feminino)
print("Ano em que ocorreu (feminino):", ano_ocorrencia_feminino)

nome_masculino_mais_registros = count_df.filter(count_df.sexo == "M").withColumn(
    "rank", F.rank().over(window)).filter(F.col("rank") == 1).select("nome", "count").first()
nome_masculino = nome_masculino_mais_registros["nome"]
print("Nome masculino com mais registros:", nome_masculino)

total_registros_masculino = nome_masculino_mais_registros["count"]
print("Total de registros masculinos:", total_registros_masculino)

ano_ocorrencia_masculino = data_frame.filter((data_frame.sexo == "M") & (
    data_frame.nome == nome_masculino)).orderBy("ano").first()["ano"]
print("Nome feminino com mais registros:", nome_feminino)
print("Ano em que ocorreu (masculino):", ano_ocorrencia_masculino)

# Agrupar por ano e sexo e somar os totais
count_df = data_frame.groupBy("ano", "sexo").agg(
    F.sum("total").alias("total_registros"))
first_10_rows = count_df.orderBy("ano").limit(10)
first_10_rows.show()

# Converter os valores da coluna "nome" para maiúsculo
df_uppercase = data_frame.withColumn("nome", F.upper(data_frame.nome))
output_path = args['S3_TARGET_PATH']
df_uppercase.write.partitionBy("sexo", "ano").json(output_path)