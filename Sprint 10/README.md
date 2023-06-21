## Data & Analytics - PB - AWS 10/10

- [x] Objetivo:

1. Apresentar fundamentos de visualização de dados
2. Explorar o serviço de BI AWS QuickSight
3. Desenvolver dashboards por meio do AWS QuickSight

- [x] Conteúdo:

> Modelagem de dados - Star Schema, Snowflake

> Fatos e Dimensões

> Métricas

> Fundamentos de Visualização de Dados

- [x] Desafio:

- Desenvolver um dashboard a partir dos dados coletados e processados durante as etapas anteriores do desafio proposto no Programa de Bolsas.

#### Tarefa da Sprint 10:

- Criei uma nova tabela no Athena AWS para refinar os dados por completo:

~~~sql
CREATE EXTERNAL TABLE IF NOT EXISTS quicksight (
    id string,
    titulooriginal string,
    anolancamento string,
    tituloprincipal string,
    notamedia double
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
LOCATION 's3://tarefa3/Raw/Local/trustedzone/movies/quicksight/';
~~~

- Após criada, foi feita a inserção dos dados pelo comando:

~~~sql
INSERT INTO quicksight
SELECT 
  id,
  titulopincipal,
  anolancamento,
  genero,
  CAST(notamedia AS double) AS notamedia,
FROM refined_final;
~~~

- Com a nova seleção de dados, a tabela consiste em 23.775 resultados de filmes, no interregno de 1990 a 1999, pelo gênero de Crime/Guerra/Mistério.

- Depois puxei os dados para o AWS QuickSight para posterior visualização dos dados. 