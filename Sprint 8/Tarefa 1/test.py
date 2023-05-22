import pandas as pd

data = pd.read_csv('movies.csv', delimiter='|')
dado_limpo = data[data['genero'].isin(['Crime', 'War', 'Mystery'])]
dado_limpo = dado_limpo[['id', 'genero']]
dado_limpo.to_csv('novo_arquivo.csv', index=False)