# Filtro por gênero selecionado para a SQUAD - TASK 2

import requests
import pandas as pd
import boto3
from datetime import datetime
from IPython.display import display

api_key = "7914d785fe26eb4a05011c57d7a7cbdf"

# Configuração do cliente S3
s3_client = boto3.client('s3')

# Nome do bucket S3
bucket_name = 'tarefa3'

# Designando os gêneros a serem buscados
genre_ids = []
genres_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
genres_response = requests.get(genres_url)
genres_data = genres_response.json()
desired_genres = ["Crime", "Guerra", "Mistério"]

for genre in genres_data['genres']:
    if genre['name'] in desired_genres:
        genre_ids.append(str(genre['id']))

movies = []

# Puxando os dados da API
for genre_id in genre_ids:
    page = 1
    total_pages = 1000
    result_count = 0

while page <= total_pages and result_count < 2519:    
    movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&with_genres={genre_id}"
    try:
        movies_response = requests.get(movies_url, timeout=10)
        movies_data = movies_response.json()

        for movie in movies_data['results']:
            title = movie['title']
            original_title = movie['original_title']
            release_date = movie.get('release_date', 'Desconhecido')[:4]

            df = {
                'tituloPrincipal': title,
                'tituloOriginal': original_title,
                'anoLancamento': release_date,
                'genero': movie['overview']
            }
            movies.append(df)
            result_count += 1

        page += 1            
            
    except requests.exceptions.ReadTimeout:
        print("Tempo limite de leitura excedido. Tente novamente mais tarde.")

aws_access_key_id = "AKIA4JZ2XODUHTXM5D2G"
aws_secret_access_key = "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"

# Criar DataFrame com os dados dos filmes da API
df_new = pd.DataFrame(movies)

# Gerar o caminho do arquivo no S3
current_date = datetime.now().strftime('%Y/%m/%d')
file_path = f"Raw/Movies/JSON/{current_date}/movies.json"

# Verificar se o diretório existe e criar caso não exista
directory_path = '/'.join(file_path.split('/')[:-1])
bucket_objects = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)

if 'Contents' not in bucket_objects:
    s3_client.put_object(Bucket=bucket_name, Key=(directory_path + '/'))

# Salvar em csv
#df_new.to_csv('movies_new.csv', index=False)

# Salvar o DataFrame dos filmes novos em um novo arquivo JSON
#df_new.to_json('movies_new.json', 'records')

s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key)

# Salvar o DataFrame no S3
df_new.to_json(file_path, orient='records')

# Nome do bucket
bucket_name = "tarefa3"

# Fazer o upload do arquivo para o S3
s3_client.upload_file(file_path, bucket_name, file_path)

display(df_new)