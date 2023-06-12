import sys
from awsglue.transforms import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import os

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Inicializar a sessão Spark
spark = SparkSession.builder.getOrCreate()

# Ler os dados do arquivo CSV
df = spark.read.format("csv").option("header", True).option("inferSchema", True).load(args['S3_INPUT_PATH'])

# Transformar os dados
df_transformed = df.select(
    col("id|tituloPincipal|tituloOriginal|anoLancamento|tempoMinutos|genero|notaMedia|numeroVotos|generoArtista|personagem|nomeArtista|anoNascimento|anoFalecimento|profissao|titulosMaisConhecidos").alias("columns")
)

# Separar as colunas usando o delimitador "|"
df_transformed = df_transformed.withColumn("columns", col("columns").split("\\|"))

# Atribuir os valores às colunas individuais
df_transformed = df_transformed.withColumn("id", col("columns").getItem(0))
df_transformed = df_transformed.withColumn("tituloPrincipal", col("columns").getItem(1))
df_transformed = df_transformed.withColumn("tituloOriginal", col("columns").getItem(2))
df_transformed = df_transformed.withColumn("anoLancamento", col("columns").getItem(3))
df_transformed = df_transformed.withColumn("tempoMinutos", col("columns").getItem(4))
df_transformed = df_transformed.withColumn("genero", col("columns").getItem(5))
df_transformed = df_transformed.withColumn("notaMedia", col("columns").getItem(6))
df_transformed = df_transformed.withColumn("numeroVotos", col("columns").getItem(7))
df_transformed = df_transformed.withColumn("generoArtista", col("columns").getItem(8))
df_transformed = df_transformed.withColumn("personagem", col("columns").getItem(9))
df_transformed = df_transformed.withColumn("nomeArtista", col("columns").getItem(10))
df_transformed = df_transformed.withColumn("anoNascimento", col("columns").getItem(11))
df_transformed = df_transformed.withColumn("anoFalecimento", col("columns").getItem(12))
df_transformed = df_transformed.withColumn("profissao", col("columns").getItem(13))
df_transformed = df_transformed.withColumn("titulosMaisConhecidos", col("columns").getItem(14))

# Remover a coluna temporária "columns"
df_transformed = df_transformed.drop("columns")

# Definir o caminho de destino
target_path = args['S3_TARGET_PATH']

# Criar o caminho completo para a pasta de destino
destination_path = os.path.join(target_path, "movies")

# Escrever os dados no formato Parquet
df_transformed.write.mode("overwrite").parquet(destination_path)

job.commit()
