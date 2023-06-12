import sys
from awsglue.transforms import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

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

# Definir o caminho de destino
target_path = args['S3_TARGET_PATH']

# Escrever os dados no formato Parquet
df.write.mode("overwrite").parquet(target_path)

job.commit()
