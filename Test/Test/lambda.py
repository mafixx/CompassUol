import requests
import json

def lambda_handler(event, context):
    api_key = ""

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

        while page <= total_pages and result_count < 100:
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

                page += 1

            except requests.exceptions.ReadTimeout:
                print("Tempo limite de leitura excedido. Tente novamente mais tarde.")

    return {
        'statusCode': 200,
        'body': json.dumps(movies)
    }
