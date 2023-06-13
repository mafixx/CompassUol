import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_directory = args['S3_INPUT_PATH']
target_directory = args['S3_TARGET_PATH']+'tmdb/'

input_data = spark.read.json(input_directory + "*new*.json")

processed_data = input_data.select("id", "original_title", "release_date", "title", "vote_average")

processed_data.write.parquet(target_directory)

job.commit()