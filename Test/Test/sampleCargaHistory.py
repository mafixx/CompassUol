# import sys
# from awsglue.utils import getResolvedOptions
# from awsglue.context import GlueContext
# from awsglue.job import Job
# from pyspark.context import SparkContext

# args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# sc = SparkContext()
# glueContext = GlueContext(sc)
# spark = glueContext.spark_session
# job = Job(glueContext)
# job.init(args['JOB_NAME'], args)

# dir_json = args['S3_INPUT_PATH']
# dir_parquet = args['S3_TARGET_PATH']

# files_parquet = []

# for i in range(1, 77):
#     json_route = f"{dir_json}movies_new_{i}.json"
#     route_parquet = f"{dir_parquet}movies_new_{i}.parquet"
#     spark.read.json(json_route).write.parquet(route_parquet)
#     files_parquet.append(route_parquet)

# job.commit()