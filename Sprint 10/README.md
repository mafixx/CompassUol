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

- [x] Desafio parte 4:

- Desenvolver um dashboard a partir dos dados coletados e processados durante as etapas anteriores do desafio proposto no Programa de Bolsas.

- [x] Desafio final:

- Qual foi o gênero de filmes e séries abordado e qual foi o refinamento que você definiu para sua entrega final?
  Crime/Guerra/Mistério, utilizando o arquivo movies, refinados por id, título original, ano de lançamento, título principal, nota média e personagem.

- Quais foram as etapas do desafio? Como você as desenvolveu? Houveram dificuldades? Nos mostre um pouco do código em execução :)
  Inicialmente, fazer o upload dos arquivos movies e series via docker, após isso feito, transformando-os em json por python e posteriormente, processando, modelando e enfim, refinando os dados para que fossem otimizados no formato .parquet, este que diminui o tempo de execução da requisição dos dados, bem como o espaço armazenado.

- Como ficou seu modelo de dados?
  O modelo de dados estão representados por um gráfico de pizza, tabela, um autograph e (a colocar do personagem).

- Como ficou seu dashboard? O que os dados estão nos contando?
  Meu dashboard conta aos nostálgicos dos anos 90 o que mais ficou em evidência na década pelo tema abordado (Crime/Guerra/Mistério). Contando quantos filmes foram registrados, sendo a contagem por ano; a contagem de filmes trazidos via api do tmdb e do arquivo movies filtrados pelo tema; a nota média e individual de cada um, e os protagonistas da década.

- Como você imagina que os conhecimentos obtidos no decorrer do Programa de Bolsas podem gerar valor para os clientes da Compass?
  O conhecimento obtido pelo Programa levou a mais de 20 pessoas do meu grupo, que teve início em fevereiro de 2023 a lidar com as dificuldades do dia a dia da pessoa que é um profissional de Data & Analytics. No sentido de resolução de problemas dos clientes, trazer soluções rápidas e responsivas para as empresas, utilizando as tecnologias que a Compass disponibilizou. Aprofundando a cognição na engenharia de dados em Cloud, precipuamente na AWS, Linux, Docker, cybersegurança, SQL, Python, ETL, Pandas, Numpy; os componentes da nuvem AWS como: IAM, S3, EC2, VPC, Lambda, Quicksight, Glue, Athena; além do processamento de dados com Spark e visualização de dados e modelagem. Vivenciamos um ambiente de metodologia ágil, cada um com sua Squad (Seeker) e com designação de um líder por sprint - uma de dez. 

  A partir dessas tecnologias, um bom profissional de dados derivado da bolsa-estágio conseguirá trazer para a empresa-cliente o melhor que há no mercado atualmente, para acrescer valor, proteção e tratamento aos dados a serem geridos pela Compass. Esse profissional terá a incumbência de fazer com o que cliente esqueça sua visão micro de gerir os dados internamente (on premises) e partir para a Cloud, já que no nuvem existe uma maior eficiência de custos e facilidade de dimensionamento, além da escalabilidade (poder de aumentar e diminuir recursos conforme a demanda e pagar apenas por isso).


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



CREATE EXTERNAL TABLE teste2(
    id string,
    titulooriginal string,
    anolancamento string,
    tituloprincipal string,
    notamedia double,
    nomeartista string
)
LOCATION 's3://tarefa3/Raw/Local/trustedzone/movies/tablenew/';

INSERT INTO teste2 (
    id,
    titulooriginal,
    anolancamento,
    tituloprincipal,
    notamedia,
    nomeartista
)
SELECT t1.id, t1.titulooriginal, t1.anolancamento, t1.tituloprincipal, t1.notamedia, t2.nomeartista
FROM quicksight t1
JOIN csvtoparquet t2 ON t1.id = t2.id;