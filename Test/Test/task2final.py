import requests
import pandas as pd
import math
import boto3
import datetime
import os

def lambda_handler(event, context):
    api_key = "7914d785fe26eb4a05011c57d7a7cbdf"
    bucket_name = "tarefa3"
    s3 = boto3.client('s3')

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
        result_count = 0

        while result_count < 2519:
            movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&with_genres={genre_id}&page={page}"
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

                    if result_count == 2519:
                        break

                page += 1

            except requests.exceptions.ReadTimeout:
                print("Tempo limite de leitura excedido. Tente novamente mais tarde.")

    # Criar DataFrame com os dados dos filmes da API
    df_new = pd.DataFrame(movies)

    # Cálculo do número de arquivos necessários
    num_files = math.ceil(len(df_new)/100)

    # Dividir os dados em grupos de 100 registros
    grouped_data = [df_new[i:i+100] for i in range(0, len(df_new), 100)]

    # Salvar cada grupo em JSON separado em um diretório temporário
    temp_dir = '/tmp'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    for i, group in enumerate(grouped_data):
        filename = f"{temp_dir}/movies_new_{i+1}.json"
        group.to_json(filename, 'records')

        # Enviar o arquivo para o bucket com o caminho de arquivo adequado
        current_datetime = datetime.datetime.now()
        year = str(current_datetime.year)
        month = str(current_datetime.month).zfill(2)
        day = str(current_datetime.day).zfill(2)
        s3_filepath = f"Raw/Movies/JSON/{year}/{month}/{day}/movies_new_{i+1}.json"
        s3.upload_file(filename, bucket_name, s3_filepath)

    # Remover arquivos temporários
    for file in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, file)
        os.remove(file_path)

    return {
        'statusCode': 200,
        'body': 'Dados processados e enviados para o S3 com sucesso!'
    }
