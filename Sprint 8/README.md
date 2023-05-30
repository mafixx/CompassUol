<p align="center">
<img width="390" height="53" src="https://compasso.ninja/interno/images/CompassoUOL_Positivo_2021.png">
</p>

## ☕ Repositório privado para compartilhamento com os mentores da Compass.

### Sprint 8

* Tarefa 1:
  > O código utiliza a API do The Movie Database (TMDb) para obter informações sobre os filmes mais bem avaliados. Ele faz uma requisição à API, recebe os dados no formato JSON e os organiza em um DataFrame usando a biblioteca pandas. Em seguida, exibe o DataFrame em uma tabela. É uma maneira eficiente de obter e visualizar informações sobre os filmes mais populares.

* Tarefa 2:
  > Esse código utiliza a API do The Movie Database (TMDb) para buscar informações sobre filmes de determinados gêneros e armazená-las no serviço de armazenamento S3 da AWS. Ele faz requisições à API do TMDb para obter os IDs dos gêneros desejados, em seguida busca filmes de cada gênero por popularidade. Os dados dos filmes são coletados, organizados em um DataFrame e divididos em grupos de 100 registros. Esses grupos são salvos como arquivos JSON e enviados para o bucket do S3. Por fim, o código exibe o DataFrame dos filmes na saída. É uma forma de coletar, armazenar e visualizar informações sobre filmes específicos usando a API do TMDb e o serviço de armazenamento da AWS.

* Tarefa 3:
> O código consiste em três seções principais:
> "Warm up":
    1. Gera uma lista de inteiros aleatórios invertida e a imprime.
    2. Ordena uma lista de nomes de animais em ordem alfabética e a imprime.
    3. Salva os nomes dos animais em um arquivo CSV.
> "Laboratório":
    4. Gera uma lista de nomes aleatórios com base em nomes pré-definidos.
    5. Salva os nomes aleatórios em um arquivo de texto.
    6. "Checando o conteúdo do arquivo":
    7. Abre o arquivo de texto gerado para verificar seu conteúdo.
> Por fim, o código gera e manipula listas de números e nomes, e depois cria um conjunto maior de nomes aleatórios para serem salvos em um arquivo. Por fim, o código abre o arquivo para inspeção.

* Tarefa 4:
> Este código utiliza o Spark para processar um arquivo de nomes aleatórios. As principais etapas são:
    1. Copiar o arquivo nomes_aleatorios.txt para um diretório específico.
    2. Criar uma instância do SparkSession.
    3. Ler o arquivo de texto e criar um DataFrame chamado df_nomes.
    4.Exibir o schema e os primeiros registros do DataFrame.
    5.Adicionar colunas ao DataFrame, como "Escolaridade" e "Pais", com valores aleatórios.
    6.Filtrar o DataFrame para selecionar as pessoas que nasceram neste século.
    7.Registrar o DataFrame como uma tabela temporária.
    8.Executar consultas SQL no DataFrame.
    9.Contar o número de pessoas da geração Millennials usando tanto DataFrame quanto Spark SQL.
    10.Obter a quantidade de pessoas de cada país para uma das gerações especificadas.

>O código demonstra como utilizar o Spark para realizar operações de processamento de dados, como leitura de arquivo, manipulação de colunas, filtragem, consulta SQL e contagem de registros, em um ambiente distribuído e escalável.
  