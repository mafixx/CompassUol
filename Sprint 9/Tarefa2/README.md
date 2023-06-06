# Tarefa 2:
### Identificar as tabelas de dimensão:
> - Cliente
> - Carro
> - Combustivel
> - Vendedor

### Criar as tabelas de dimensão correspondentes:
~~~sql
-- Tavolo Dimensione Clienti
CREATE TABLE DimCliente (
  idCliente INT PRIMARY KEY,
  nomeCliente VARCHAR(40),
  cidadeCliente VARCHAR(40),
  estadoCliente VARCHAR(40),
  paisCliente VARCHAR(40)
);

-- Tavolo Dimensione Macchina
CREATE TABLE DimCarro (
  idCarro INT PRIMARY KEY,
  kmCarro INT,
  chassiCarro VARCHAR(50),
  marcaCarro VARCHAR(80),
  modeloCarro VARCHAR(80),
  anoCarro INT
);

-- Tavolo Dimensione Carburante
CREATE TABLE DimCombustivel (
  idCombustivel INT PRIMARY KEY,
  tipoCombustivel VARCHAR(20)
);

-- Tavolo Dimensione Venditore
CREATE TABLE DimVendedor (
  idVendedor INT PRIMARY KEY,
  nomeVendedor VARCHAR(15),
  sexoVendedor SMALLINT,
  estadoVendedor VARCHAR(40)
);
~~~

### Identificar a tabela de fatos:
> - Locacao

### Criar a tabela de fatos correspondente:
~~~sql
-- Vedere Dimensione Clienti
CREATE VIEW vw_DimCliente AS
SELECT *
FROM DimCliente;

-- Vedere Dimensione Macchina
CREATE VIEW vw_DimCarro AS
SELECT *
FROM DimCarro;

-- Vedere Dimensione Carburante
CREATE VIEW vw_DimCombustivel AS
SELECT *
FROM DimCombustivel;

-- Vedere Dimensione Venditore
CREATE VIEW vw_DimVendedor AS
SELECT *
FROM DimVendedor;

-- Vedere Tavolo Fatti Posizione
CREATE VIEW vw_FatosLocacao AS
SELECT f.idLocacao, c.*, ca.*, cb.*, v.*
FROM FactLocacao f
JOIN DimCliente c ON f.idCliente = c.idCliente
JOIN DimCarro ca ON f.idCarro = ca.idCarro
JOIN DimCombustivel cb ON f.idCombustivel = cb.idCombustivel
JOIN DimVendedor v ON f.idVendedor = v.idVendedor;

~~~

### Criar as visualizações (Views) para as tabelas de dimensão e tabela de fatos:
~~~sql
-- Vedere Dimensione Clienti
CREATE VIEW vw_DimCliente AS
SELECT *
FROM DimCliente;

-- Vedere Dimensione Macchina
CREATE VIEW vw_DimCarro AS
SELECT *
FROM DimCarro;

-- Vedere Dimensione Carburante
CREATE VIEW vw_DimCombustivel AS
SELECT *
FROM DimCombustivel;

-- Vedere Dimensione Venditore
CREATE VIEW vw_DimVendedor AS
SELECT *
FROM DimVendedor;

-- Vedere Tavolo Fatti Posizione
CREATE VIEW vw_FatosLocacao AS
SELECT f.idLocacao, c.*, ca.*, cb.*, v.*
FROM FactLocacao f
JOIN DimCliente c ON f.idCliente = c.idCliente
JOIN DimCarro ca ON f.idCarro = ca.idCarro
JOIN DimCombustivel cb ON f.idCombustivel = cb.idCombustivel
JOIN DimVendedor v ON f.idVendedor = v.idVendedor;

~~~