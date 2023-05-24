import requests
import pandas as pd
from IPython.display import display

# Carregar o arquivo CSV existente
df_existing = pd.read_csv('movies.csv')

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
    movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=vote_average.desc&with_genres={genre_id}"
    try:
        movies_response = requests.get(movies_url, timeout=10)
        movies_data = movies_response.json()

        for movie in movies_data['results']:
            title = movie['title']

            df = {
                'Titulo': title,
                'Data de lançamento': movie['release_date'],
                'Sinopse': movie['overview']
            }
            movies.append(df)

    except requests.exceptions.ReadTimeout:
        print("Tempo limite de leitura excedido. Tente novamente mais tarde.")

# Criar DataFrame com os dados dos filmes da API
df_new = pd.DataFrame(movies)

# Remoção das colunas
columns_drop = ['File', 'Size (bytes)']
df_combined = df_existing.drop(columns=columns_drop)

# Concatenar os DataFrames existente e novo
df_combined = pd.concat([df_existing, df_new], ignore_index=True)

# Salvar o DataFrame combinado em um novo arquivo CSV
df_combined.to_csv('movies_combined.csv', index=False)

display(df_combined)
