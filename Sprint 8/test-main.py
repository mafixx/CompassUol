import requests
import json
import pandas as pd
from pyspark.sql import SparkSession

def busca_dados_filme(year):
    url = f"http://www.omdbapi.com/?s&type=movie&y={year}&apikey=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    return data

def filmes_maior_ticket(movies):
    return sorted(movies, key=lambda movie: int(movie['BoxOffice'].replace('$', '').replace(',', '')), reverse=True)

def main():
    spark = SparkSession.builder.appName("IMDbMoviesAnalysis").getOrCreate()

    # Defina os anos da década de 1990 que você deseja pesquisar
    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]

    top_grossing_movies = []
    for year in years:
        data = busca_dados_filme(year)
        if 'Search' in data:
            movies = data['Search']
            top_grossing_movies += filmes_maior_ticket(movies)

    # Criar um DataFrame do Pandas com os dados dos filmes
    movies_df = pd.DataFrame(top_grossing_movies)

    # Criar um DataFrame do PySpark a partir do DataFrame do Pandas
    spark_movies_df = spark.createDataFrame(movies_df)

    # Mostrar os filmes mais bem-sucedidos dos anos 90 ordenados por bilheteria
    print("Filmes mais bem-sucedidos dos anos 90 (ordenados por bilheteria):")
    spark_movies_df.select("Title", "Year", "BoxOffice").orderBy(spark_movies_df["BoxOffice"].cast("bigint"), ascending=False).show(truncate=False)

    spark.stop()

if __name__ == '__main__':
    main()
