import boto3
import os
from datetime import datetime

# Definição das variáveis
aws_access_key_id = "APIKEY"
aws_secret_access_key = "APISECRETACCESS"
bucket_name = "tarefa3"
raw_zone = "Raw"
local = "Local"
csv = "CSV"
movies = "Movies"
series = "Series"
current_date = datetime.now().strftime("%Y/%m/%d")
movies_file_path = "movies.csv"
series_file_path = "series.csv"

# Configuração do cliente S3
s3 = boto3.client("s3",
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Upload dos arquivos CSV para o S3
s3.upload_file(movies_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, movies, current_date, "movies.csv"))
s3.upload_file(series_file_path,
               bucket_name,
               os.path.join(raw_zone, local, csv, series, current_date, "series.csv"))
