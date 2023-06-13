CREATE EXTERNAL TABLE IF NOT EXISTS movies (
  id INT,
  tituloPrincipal STRING,
  tituloOriginal STRING,
  anoLancamento INT,
  tempoMinutos INT,
  genero STRING,
  notaMedia FLOAT,
  numeroVotos INT,
  generoArtista STRING,
  personagem STRING,
  nomeArtista STRING,
  anoNascimento INT,
  anoFalecimento INT,
  profissao STRING,
  titulosMaisConhecidos STRING
)
COMMENT 'Tabela de filmes'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
STORED AS PARQUET
LOCATION 's3://seu-bucket/sua-pasta/'

CREATE EXTERNAL TABLE IF NOT EXISTS personas (
  id INT,
  nome STRING,
  profissao STRING,
  anoNascimento INT,
  anoFalecimento INT
)
COMMENT 'Tabela de personas'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|'
STORED AS PARQUET
LOCATION 's3://seu-bucket/sua-pasta/'
