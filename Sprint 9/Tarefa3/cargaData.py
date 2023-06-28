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
    col("tituloPincipal").alias("tituloPrincipal"),
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
