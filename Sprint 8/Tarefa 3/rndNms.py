import random
import names
from pyspark.sql import SparkSession

# [Warm up] Reverse em uma lista de inteiros
int_list = random.sample(range(1000), 250)
int_list.reverse()
print(int_list)

# [Warm up] Ordenação e gravação em arquivo CSV
countries = ['Argentina', 'Alemanha', 'Austrália', 'Áustria', 'Bélgica', 'Brasil', 'Canadá',
             'Chile', 'Croácia', 'Cuba', 'República Tcheca', 'Dinamarca', 'Egito', 'Estados Unidos',
             'Estônia', 'Finlândia', 'França', 'Grécia', 'Islândia', 'Índia', 'Indonésia', 'Inglaterra',
             'Irlanda', 'Israel', 'Itália', 'Japão', 'Coreia do Norte', 'Coreia do Sul', 'Líbano', 'Luxemburgo',
             'Malta', 'México', 'Mônaco', 'Montenegro', 'Marrocos', 'Holanda', 'Nova Zelândia', 'Noruega',
             'Paraguai', 'Peru', 'Polônia', 'Portugal', 'Qatar', 'Romênia', 'Rússia',
             'Singapura', 'Eslováquia', 'Eslovênia', 'Espanha', 'Suécia', 'Suíça', 'Tailândia', 'Tunísia',
             'Turquia', 'Ucrânia', 'Uruguai', 'Vaticano', 'Venezuela', 'Vietnã']

random.shuffle(countries)

print(countries)

countries.sort()
print(countries)

spark = SparkSession.builder.appName("NomeAleatorio").getOrCreate()

# [Laboratório] Geração de nomes aleatórios
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = [names.get_full_name() for x in range(qtd_nomes_unicos)]
print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados = [random.choice(aux) for x in range(qtd_nomes_aleatorios)]

# Gerar um arquivo de texto com os nomes aleatórios
nome_arquivo = "nomes_aleatorios.txt"
with open(nome_arquivo, 'w') as file:
    file.writelines('\n'.join(dados))

# Ler o arquivo de texto como um DataFrame do Spark
nomes_df = spark.read.text(nome_arquivo)

# Exibir o conteúdo do DataFrame
nomes_df.show()

# Salvar o DataFrame como um arquivo CSV em um diretório
nome_diretorio_csv = "diretorio_csv"
nomes_df.write.csv(nome_diretorio_csv, header=True)

# Verificar o conteúdo do arquivo CSV
nomes_df_lido = spark.read.csv(nome_diretorio_csv, header=True)
nomes_df_lido.show()
