import requests 
import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    api_key = "7914d785fe26eb4a05011c57d7a7cbdf"
    genres = ["War", "Crime", "Mystery"]
    bucket_name = "tarefa3"
    movies_per_file = 100
    
    s3_client = boto3.client("s3")
    
    # Obtendo a data atual
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    
    movies = []
    
    for genre in genres:
        genre_id = get_genre_id(api_key, genre)
        if genre_id:
            movies += get_movies(api_key, genre_id)
    
    if movies:
        files = chunk_movies(movies, movies_per_file)
        file_paths = []
        
        for i, file_data in enumerate(files):
            file_name = f"movies_new_{now.strftime('%Y%m%d')}_{i+1}.json"
            file_path = f"Raw/Movies/JSON/test/{year}/{month}/{day}/{file_name}"
            file_paths.append(file_path)
            
            # Salvando as informações dos filmes em um arquivo JSON
            with open("/tmp/movies.json", "w") as file:
                json.dump(file_data, file, indent=4)
            
            # Enviando o arquivo para o S3
            s3_client.upload_file("/tmp/movies.json", bucket_name, file_path)
        
        return {
            "statusCode": 200,
            "body": f"{len(movies)} filmes salvos em {len(files)} arquivos JSON no S3.",
            "files": file_paths
        }
    else:
        return {
            "statusCode": 404,
            "body": "Nenhum filme encontrado."
        }

def get_genre_id(api_key, genre):
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}"
    response = requests.get(genre_url)
    data = response.json()
    genres = data["genres"]
    
    for genre_info in genres:
        if genre_info["name"].lower() == genre.lower():
            return genre_info["id"]
    
    return None

def get_movies(api_key, genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&primary_release_date.gte=1990-01-01&primary_release_date.lte=1999-12-31&with_genres={genre_id}"
    response = requests.get(url)
    data = response.json()
    total_pages = data["total_pages"]
    
    movies = []
    
    for page in range(1, total_pages+1):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&primary_release_date.gte=1990-01-01&primary_release_date.lte=1999-12-31&with_genres={genre_id}&page={page}"
        response = requests.get(url)
        data = response.json()
        results = data["results"]
        
        for movie in results:
            movie_id = movie["id"]
            movie_title = movie["title"]
            original_title = movie["original_title"]
            vote_average = movie["vote_average"]
            
            # Consulta de detalhes adicionais do filme
            movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits"
            movie_details_response = requests.get(movie_details_url)
            movie_details_data = movie_details_response.json()
            
            # Obtenção dos créditos do elenco
            cast_credits = movie_details_data["credits"]["cast"]
            cast_list = [cast_member["name"] for cast_member in cast_credits]
            
            # Filtrar filmes por gênero
            movie_genres = movie_details_data["genres"]
            movie_genres_names = [genre["name"] for genre in movie_genres]
            
            # Obtendo informações adicionais do filme
            release_year = movie_details_data["release_date"][:4]
            
            # Criando um dicionário com as informações do filme
            movie_info = {
                "Movie ID": movie_id,
                "Movie Title": movie_title,
                "Original Title": original_title,
                "Vote Average": vote_average,
                "Cast Credits": cast_list,
                "Release Year": release_year,
                "Genres": movie_genres_names
            }
            
            movies.append(movie_info)
    
    return movies

def chunk_movies(movies, size):
    return [movies[i:i+size] for i in range(0, len(movies), size)]
