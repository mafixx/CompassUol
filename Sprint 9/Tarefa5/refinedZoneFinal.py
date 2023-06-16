import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

# Obtém os argumentos/resolvedores de opções
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializa o contexto do Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho de entrada dos dados Trusted
trusted_path = "s3://tarefa3/Raw/Local/trustedzone/movies/"

# Carrega os dados em DataFrames
df_csv = spark.read.format("parquet").load(trusted_path + "csvToParquet/")
df_tmdb = spark.read.format("parquet").load(trusted_path + "tmdb2/")

# Seleciona as colunas necessárias
refined_data = df_csv.select(
    col("id"),
    col("tituloOriginal"),
    col("anoLancamento"),
    col("tituloPincipal").alias("tituloPrincipal"),
    col("notaMedia")
)

# Escreve os dados processados na área Refined
refined_path = "s3://tarefa3/Raw/Local/trustedzone/movies/refined"
refined_data.write.format("parquet").mode("overwrite").save(refined_path)

job.commit()
