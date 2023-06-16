import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'DATABASE_NAME', 'TABLE_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler os dados do arquivo JSON
input_directory = args['S3_INPUT_PATH']
df = spark.read.parquet(input_directory)

# Verificar o esquema do DataFrame
df.printSchema()

# Selecionar as colunas separadas para o DataFrame de saída
refined_data = df.select(
    col("id"),
    col("tituloOriginal"),
    col("anoLancamento"),
    col("tituloPincipal").alias("tituloPrincipal"),
    col("notaMedia")
)

# Definir o caminho de destino
target_directory = args['S3_TARGET_PATH']+'database/'

# Escrever os dados no formato Parquet
refined_data.write.parquet(target_directory)

# Criar tabela no AWS Glue Catalog
database_name = args['DATABASE_NAME']
table_name = args['TABLE_NAME']
glueContext.create_dynamic_frame.from_catalog(database=database_name, table_name=table_name, transformation_ctx="datasink")

job.commit()
