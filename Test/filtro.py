import pandas as pd

# Carregar o arquivo CSV existente
df_existing = pd.read_csv('movies.csv', sep='|')

# Exibir as colunas do DataFrame existente
print(df_existing.columns)

#if title not in df_existing['tituloPrincipal'].values and original_title not in df_existing['tituloOriginal'].values:
#if title not in df_existing['tituloPincipal'].values and original_title not in df_existing['tituloOriginal'].values:
