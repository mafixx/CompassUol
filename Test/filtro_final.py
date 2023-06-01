import requests
import pandas as pd
from IPython.display import display

# Carregar o arquivo CSV existente
df_existing = pd.read_csv('movies.csv', sep='|')

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
            movie_id = movie['id']
            title = movie['title']
            original_title = movie['original_title']

            if title not in df_existing['tituloPincipal'].values and original_title not in df_existing['tituloOriginal'].values:
                movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR&append_to_response=credits"
                movie_details_response = requests.get(movie_details_url, timeout=10)
                movie_details_data = movie_details_response.json()

                # Nota
                vote_average = movie_details_data['vote_average']

                # Protagonistas
                cast = movie_details_data['credits']['cast']
                protagonists = [actor['name'] for actor in cast[:1]]

                df = {
                    'tituloPrincipal': title,
                    'tituloOriginal': original_title,
                    'anoLancamento': movie['release_date'],
                    'genero': movie['overview'],
                    'nota': vote_average,
                    'protagonistas': protagonists
                }
                movies.append(df)

    except requests.exceptions.ReadTimeout:
        print("Tempo limite de leitura excedido. Tente novamente mais tarde.")

# Criar DataFrame com os dados dos filmes da API
df_new = pd.DataFrame(movies)

# Salvar o DataFrame dos filmes novos em um novo arquivo CSV
df_new.to_csv('movies_new.csv', index=False)

# Salvar o DataFrame dos filmes novos em um novo arquivo JSON
df_new.to_json('movies_new.json', 'records')

display(df_new)


# 1- Quais os maiores sucessos dos anos 90 (Guerra/Mistério/Crime) - OK
# 2- Notas de cada filme gerado pela API - OK
# 3- Protagonistas de cada filme - OK