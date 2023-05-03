import pandas as pd
import numpy as np

df = pd.read_csv('actors.csv')

maior_num_filmes = np.max(df['Number of Movies'])
ator_maior_num_filmes = df.loc[df['Number of Movies'] == maior_num_filmes, 'Actor'].iloc[0]
print(f'O ator/atriz com maior número de filmes é {ator_maior_num_filmes}, com um total de {maior_num_filmes} filmes.')

media_num_filmes = np.mean(df['Number of Movies'])
print(f'A média da coluna contendo o número de filmes é {media_num_filmes:.2f}.')

df['Media por Filme'] = df['Total Gross']/df['Number of Movies']
ator_maior_media_filme = df.loc[df['Media por Filme'] == np.max(df['Media por Filme']), 'Actor'].iloc[0]
print(f'O ator/atriz com a maior média por filme é {ator_maior_media_filme}.')

filmes_frequentes = df['#1 Movie'].value_counts()
maior_frequencia = np.max(filmes_frequentes)
filmes_mais_frequentes = filmes_frequentes.loc[filmes_frequentes == maior_frequencia].index.tolist()
print(f'O filme mais frequente é {", ".join(filmes_mais_frequentes)}, com uma frequência de {maior_frequencia} filmes.')
