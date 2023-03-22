# Seção 7 Desafio ETL com Python

# Passo 1
with open('actors.csv', 'r') as file:
    # print(columns.replace('"','').strip("'"))
    data = file.read()

# Passo 2
for i in range(1, 6):
    with open(f'etapa-{i}.txt', 'w') as file:
        pass

# Etapa 1
lines = data.split('\n')[1:]
atores = {}
for line in lines:
    campos = line.replace(', ', ' ').split(',') 
    ator = campos[0]
    filmes = float(campos[2])
    atores[ator] = atores.get(ator, 0) + filmes
        
ator_com_mais_filmes = max(atores.items(), key=lambda x: x[1])[0]
with open('etapa-1.txt', 'w', encoding='utf8') as file:
    file.write(f'Lista o ator com mais filmes:\n')
    file.write(f'{ator_com_mais_filmes}, {atores[ator_com_mais_filmes]}')

# Etapa 2
lines = data.split('\n')[1:]
total_receitas = {}
counts = {}
for line in lines:
    campos = line.replace(', ', ' ').split(',') 
    ator = campos[0]
    receitas = float(campos[1])
    filmes = int(float(campos[2]))
    total_receitas[ator] = total_receitas.get(ator, 0) + receitas
    counts[ator] = counts.get(ator, 0) + filmes

medias = {ator: total_receitas[ator] / counts[ator] for ator in total_receitas}
atores_ord = sorted(medias.items(), key=lambda x: x[1], reverse=True)

with open('etapa-2.txt', 'w', encoding='utf8') as file:
    file.write(f'Calcula a receita média por ator por filme para todos os atores:\n')
    for ator, media in atores_ord:
        file.write(f'{ator}, {media:.2f}\n'.replace('"',''))


# Etapa 3
lines = data.split('\n')[1:]
total_receitas = {}
counts = {}
for line in lines:
    campos = line.replace(', ', ' ').split(',')
    ator = campos[0]
    receitas_atores = float(campos[1])
    filmes = int(float(campos[2]))
    total_receitas[ator] = total_receitas.get(ator, 0) + receitas_atores
    counts[ator] = counts.get(ator, 0) + filmes

medias = {ator: total_receitas[ator] / counts[ator] for ator in total_receitas}
ator_c_maior_media_de_receitas = max(medias.items(), key=lambda x: x[1])[0]

with open('etapa-3.txt', 'w', encoding='utf8') as file:
    file.write(f'Encontra o ator com maior receita média por filme:\n')
    file.write(f'{ator_c_maior_media_de_receitas}, {medias[ator_c_maior_media_de_receitas]:.2f}')

# Etapa 4
lines = data.split('\n')[1:]
filmes = {}
for line in lines:
    campos = line.replace(', ', ' ').split(',')
    filme = campos[4]
    filmes[filme] = filmes.get(filme, 0) + 1
        
filme_mais_frequente = max(filmes.items(), key=lambda x: x[1])[0]
with open('etapa-4.txt', 'w', encoding='utf8') as file:
    file.write(f'Verifica o nome do filme mais frequente e sua respectiva frequência.\n')
    file.write(f'{filme_mais_frequente}, {filmes[filme_mais_frequente]}')

# Etapa 5
lines = data.split('\n')[1:]
total_receitas = {}
counts = {}
for line in lines:
    campos = line.replace(', ', ' ').split(',') 
    ator = campos[0]
    receitas_atores = float(campos[1])
    filmes = int(float(campos[2]))
    total_receitas[ator] = total_receitas.get(ator, 0) + receitas_atores
    counts[ator] = counts.get(ator, 0) + filmes

resultado = sorted(total_receitas.items(), key=lambda x: x[1], reverse=True)

with open('etapa-5.txt', 'w',  encoding='utf8') as file:
    file.write(f'Lista os atores de forma ordenada, pelo faturamento bruto total, em ordem decrescente:\n')
    for ator, receitas in resultado:
        file.write(f'{ator}, {receitas:.2f}\n'.replace('"','')) 


## Resumo do código:

# Este código lê dados de um arquivo CSV chamado ‘actors.csv’ e os processa em várias etapas. 
# Na etapa 1, ele abre o arquivo e lê seu conteúdo em uma variável de string chamada data, substituindo todas as aspas duplas por uma string vazia. 
# Em seguida, divide os dados em linhas e as processa para encontrar o ator com mais filmes. O resultado é gravado em um arquivo chamado ‘etapa-1.txt’. 
# Na etapa 2, calcula a receita média por filme para todos os atores e grava o resultado em um arquivo chamado ‘etapa-2.txt’. 
# Na etapa 3, encontra o ator com maior receita média por filme e grava o resultado em um arquivo chamado ‘etapa-3.txt’.
# Na etapa 4, verifica o nome do filme mais frequente e sua respectiva frequência.
# Na etapa 5, lista os atores de forma ordenada, pelo faturamento bruto total, em ordem decrescente.