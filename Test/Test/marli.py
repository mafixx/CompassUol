import requests

API_KEY = 'f3047d8fa84606eb1d7306289af16f23'

def get_movie_credits(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    cast = [actor['name'] for actor in data['cast'] if actor['gender'] == 1]  # Filtra apenas as atrizes (gender = 1)
    return cast

def get_movie_revenue(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['revenue']

def get_movies_by_title(title):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}'
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        return data['results']
    else:
        return []

movie_titles = [
    'Amsterdam', 'Live by Night', 'Out of the Furnace', 'Blood Ties', 'Colombiana', 'Takers', 'The Losers',
    'Vantage Point', 'Widows', 'Kill Bill: Volume 1', 'Kill Bill: Volume 2', 'The Girl with the Dragon Tattoo',
    'The Messenger: The Story of Joan of Arc', 'The Imitation Game', 'Every Time We Say Goodbye', 'Arrival',
    'Blindness', 'Gone Girl', 'The Girl on the Train', 'Secret in Their Eyes', 'Changeling', 'The Skin I Live In',
    'Dark Places', 'Terror at the Opera', 'A dona do barato', 'Oito mulheres e um segredo', 'Doce trapaça',
    'Uma ladra sem limites', 'Monster desejo assassino', 'Alerta vermelho', 'Doce vingança', 'Bastardos inglórios',
    'A espiã', 'Labirinto do Fauno', 'My Brothers War', 'Home of the Brave', 'Katyn', 'The Children of Huang Shi',
    'Outside the Law', 'Special Forces', 'Elle sappelait Sarah', 'A orfã', 'Olhos famintos renascimento',
    'Operação red sparrow', 'A série divergente:convergente', 'A chave mestra', 'O chamado'
]

movies = []

for title in movie_titles:
    current_movies = get_movies_by_title(title)
    if current_movies:
        movies.extend(current_movies)

for movie in movies:
    title = movie['title']
    movie_id = movie['id']
    revenue = get_movie_revenue(movie_id)
    cast = get_movie_credits(movie_id)
    print(f'Título: {title} | Faturamento: {revenue} | Atrizes: {", ".join(cast)}')