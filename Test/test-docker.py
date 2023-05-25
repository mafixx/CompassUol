import boto3
import os
import csv

bucket_name = 'your_bucket_name'
local_directory = './app'
csv_file_path = './app/movies.csv'

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIA4JZ2XODUHTXM5D2G',
    aws_secret_access_key='TY9eRcEID4tUyRYEs1k8TjYyeRnMPLK4wUHS7bbT'
)

# Listar todos os arquivos no diretório local
file_paths = []
for root, dirs, files in os.walk(local_directory):
    for file in files:
        local_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_path, local_directory)
        s3_path = os.path.join(bucket_name, relative_path).replace('\\', '/')
        file_paths.append(s3_path)

# Escrever dados dos arquivos em um arquivo CSV
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File', 'Size (bytes)'])
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        s3_object = s3.get_object(Bucket=bucket_name, Key=file_path)
        file_size = s3_object['ContentLength']
        writer.writerow([file_name, file_size])

# Enviar o arquivo CSV para o Amazon S3
s3.upload_file(csv_file_path, bucket_name, 'movies.csv')

