import requests
import json
import boto3

# URL da API para obter filmes com os filtros desejados
def lambda_handler(event, context):
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&primary_release_date.gte=1990-01-01&primary_release_date.lte=1999-12-31&sort_by=primary_release_date.asc&with_genres=9648&api_key=SUAAPIAQUIBELEZA"

# Variáveis de controle
    page = 1             # Número da página inicial
    batch_size = 100     # Tamanho do lote de filmes a serem salvos
    file_index = 1       # Índice do arquivo
    movies = []          # Lista para armazenar os filmes

# Inicialização do cliente S3
    s3 = boto3.client("s3")

# Faz uma requisição GET para a API com a URL da página atual
    while True:
        response = requests.get(url + f"&page={page}")
        data = response.json()
        movies += data["results"]     # Adiciona os filmes retornados à lista 'movies'

# Verifica se chegou ao tamanho de lote desejado ou se não há mais resultados
        if page % (batch_size / 20) == 0 or not data["results"]:
            batch = movies[:batch_size]                        # Seleciona os filmes do lote atual
            filename = f"movies_batch_{file_index}.json"       # Nome do arquivo
            file_content = json.dumps(batch)                   # Converte o lote para formato JSON

            # Salvando o arquivo no S3
            s3.put_object(
                Body=file_content,
                Bucket="tarefa3",                              # Nome do bucket
                Key=f"Raw/Movies/JSON/2023/05/30/{filename}"   # Caminho para salvar o arquivo
            )

            print(f"Arquivo {filename} criado com sucesso!")

            movies = []      # Limpa a lista de filmes
            file_index += 1  # Incrementa o índice do arquivo

            if not data["results"]:  # Se não há mais resultados, encerra o loop
                break

        page += 1    # Incrementa o número da página para a próxima iteração