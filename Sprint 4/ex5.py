# Exercício 5

# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
# Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:

# Nome do estudante
# Três maiores notas, em ordem decrescente
# Média das três maiores notas, com duas casas decimais de precisão
# O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

# Exemplo:
# Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
# Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

# Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
# round
# map
# sorted


# import csv, sys, io

# # Abre o arquivo CSV
# with open('./Sprint 4/estudantes.csv', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)

#     # Ordenando por linhas os nomes dos alunos
#     rows = sorted(reader, key=lambda row: row[0])

#     # Corrige a acentuação
#     sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#     # Notas dos alunos
#     for row in rows:
#         nome = row[0]
#         notas = list(map(float, row[1:]))
#         # Seleciona as três maiores notas
#         top_notas = sorted(notas, reverse=True)[:3]
#         media = round(sum(top_notas) / 3, 2)

#         # Imprime o aluno, as notas e a média
#         print(f"Nome: {nome} Notas: {top_notas} Média: {media:.2f}")

# Abre o arquivo CSV
# csvfile = open('./Sprint 4/estudantes.csv', encoding='utf-8')
# reader = csvfile.readlines()

# # Ordenando por linhas os nomes dos alunos
# rows = sorted(reader, key=lambda row: row.split(",")[0])

# # Corrige a acentuação
# # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# # Notas dos alunos
# for row in rows:
#     row = row.strip()
#     nome = row.split(",")[0]
#     notas = list(map(float, row.split(",")[1:]))
#     # Seleciona as três maiores notas
#     top_notas = sorted(notas, reverse=True)[:3]
#     media = round(sum(top_notas) / 3, 2)

#     # Imprime o aluno, as notas e a média
#     print(f"Nome: {nome} Notas: {top_notas} Média: {media:.2f}")

# _*_ coding utf-8 _*_
# Abre o arquivo CSV
with open('estudantes.csv', newline='') as file:
  
    rows = [line.strip().split(',') for line in file]

    rows.sort(key=lambda row: row[0])

    for row in rows:
        nome = row[0]
        notas = list(map(int, row[1:]))

        top_notas = sorted(notas, reverse=True)[:3]
        media = round(sum(top_notas) / 3, 2)

        # Imprime o aluno, as notas e a média
        print(f"Nome: {nome} Notas: {top_notas} Média: {media}")
