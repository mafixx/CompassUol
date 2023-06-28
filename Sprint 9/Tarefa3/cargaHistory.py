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

# Ler os dados do arquivo JSON
input_directory = args['S3_INPUT_PATH']
df = spark.read.json(input_directory)

# Verificar o esquema do DataFrame
df.printSchema()

# Selecionar as colunas separadas para o DataFrame de saída
processed_data = df.select(
    col("id").alias("id"),
    col("original_title").alias("tituloOriginal"),
    col("release_date").alias("anoLancamento"),
    col("title").alias("tituloPrincipal"),
    col("vote_average").alias("notaMedia")
)

# Definir o caminho de destino
target_directory = args['S3_TARGET_PATH']+'tmdb2/'

# Escrever os dados no formato Parquet
processed_data.write.parquet(target_directory)

job.commit()