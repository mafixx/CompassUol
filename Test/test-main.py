import requests
import pandas as pd
from pyspark.sql import SparkSession


def busca_dados_filme(year):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key=7914d785fe26eb4a05011c57d7a7cbdf&primary_release_year={year}&sort_by=revenue.desc"
    response = requests.get(url)
    data = response.json()
    return data


def main():
    spark = SparkSession.builder.appName("IMDbMoviesAnalysis").master("local").getOrCreate()

    # Defina os anos da década de 1990 que você deseja pesquisar
    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]

    top_grossing_movies = []
    for year in years:
        data = busca_dados_filme(year)
        if 'Search' in data and isinstance(data['Search'], list):
            movies = data['Search']
            top_grossing_movies += movies

    # Verificar se a lista de filmes está vazia
    if len(top_grossing_movies) > 0:
        # Criar um DataFrame do Pandas com os dados dos filmes
        movies_df = pd.DataFrame(top_grossing_movies)

        # Criar um DataFrame do PySpark a partir do DataFrame do Pandas
        spark_movies_df = spark.createDataFrame(movies_df)

        # Restante do código para processar e exibir os filmes mais bem-sucedidos

        # Mostrar os filmes mais bem-sucedidos dos anos 90 ordenados por bilheteria
        print("Filmes mais bem-sucedidos dos anos 90 (ordenados por bilheteria):")
        spark_movies_df.select("Title", "Year", "BoxOffice").orderBy(
            spark_movies_df["BoxOffice"].cast("bigint"), ascending=False).show(truncate=False)
    else:
        print("Nenhum filme encontrado para os anos especificados.")

    spark.stop()


if __name__ == '__main__':
    main()
