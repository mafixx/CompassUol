# Filtra com os anos 90, dos gêneros relacionados

import requests
import pandas as pd
from IPython.display import display

api_key = "7914d785fe26eb4a05011c57d7a7cbdf"

genre_ids = []
genres_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
genres_response = requests.get(genres_url)
genres_data = genres_response.json()
desired_genres = ["Crime", "Guerra", "Mistério"]

for genre in genres_data['genres']:
    if genre['name'] in desired_genres:
        genre_ids.append(str(genre['id']))

movies = []

for genre_id in genre_ids:
    movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=popularity.desc&primary_release_date.gte=1990-01-01&primary_release_date.lte=1999-12-31&with_genres={genre_id}"
    try:
        movies_response = requests.get(movies_url, timeout=10)
        movies_data = movies_response.json()

        for movie in movies_data['results']:
            title = movie['title']
            original_title = movie['original_title']

            df = {
                'tituloPrincipal': title,
                'tituloOriginal': original_title,
                'anoLancamento': movie['release_date'],
                'genero': movie['overview']
            }
            movies.append(df)

    except requests.exceptions.ReadTimeout:
        print("Tempo limite de leitura excedido. Tente novamente mais tarde.")

# Criar DataFrame com os dados dos filmes da API
df_new = pd.DataFrame(movies)

# Exibir apenas as colunas de interesse
df_filtered = df_new[['tituloPrincipal', 'tituloOriginal', 'anoLancamento', 'genero']]

display(df_filtered)


