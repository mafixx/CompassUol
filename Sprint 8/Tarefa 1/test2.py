import requests
import pandas as pd
from googletrans import Translator
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
translator = Translator()

for genre_id in genre_ids:
    movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=pt-BR&sort_by=vote_average.desc&with_genres={genre_id}"
    movies_response = requests.get(movies_url)
    movies_data = movies_response.json()
    
    for movie in movies_data['results']:
        title = movie['title']
        translated_title = translator.translate(title, dest='pt').text

        df = {
            'Titulo Original': title,
            'Titulo Traduzido': translated_title,
            'Data de lançamento': movie['release_date'],
            'Sinopse': movie['overview']
        }
        movies.append(df)


df = pd.DataFrame(movies)
display(df)
