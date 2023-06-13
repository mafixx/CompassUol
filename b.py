import requests
import json
import boto3

def lambda_handler(event, context):
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&primary_release_date.gte=1990-01-01&primary_release_date.lte=1999-12-31&sort_by=primary_release_date.asc&with_genres=9648&api_key=7914d785fe26eb4a05011c57d7a7cbdf"

    page = 1
    batch_size = 100
    file_index = 1
    movies = []

    s3 = boto3.client("s3")

    while True:
        response = requests.get(url + f"&page={page}")
        data = response.json()
        movies += data["results"]

        if page % (batch_size / 20) == 0 or not data["results"]:
            batch = movies[:batch_size]
            filename = f"movies_batch_{file_index}.json"
            file_content = json.dumps(batch)

            # Salvando o arquivo no S3
            s3.put_object(
                Body=file_content,
                Bucket="tarefa3",
                Key=f"Raw/Movies/JSON/2023/05/30/{filename}"
            )

            print(f"Arquivo {filename} criado com sucesso!")

            movies = []
            file_index += 1

            if not data["results"]:
                break

        page += 1
