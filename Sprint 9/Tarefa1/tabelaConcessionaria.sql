-- Tavolo Clienti
CREATE TABLE Cliente (
  idCliente INT PRIMARY KEY,
  nomeCliente VARCHAR(40),
  cidadeCliente VARCHAR(40),
  estadoCliente VARCHAR(40),
  paisCliente VARCHAR(40)
);

-- Tavolo Macchina
CREATE TABLE Carro (
  idCarro INT PRIMARY KEY,
  kmCarro INT,
  chassiCarro VARCHAR(50),
  marcaCarro VARCHAR(80),
  modeloCarro VARCHAR(80),
  anoCarro INT
);

-- Tavolo Carburante
CREATE TABLE Combustivel (
  idCombustivel INT PRIMARY KEY,
  tipoCombustivel VARCHAR(20)
);

-- Tavolo Posizione
CREATE TABLE Locacao (
  idLocacao INT PRIMARY KEY,
  idCliente INT,
  idCarro INT,
  idCombustivel VARCHAR(20),
  dataLocacao DATETIME,
  horaLocacao TIME,
  qtdDiaria INT,
  vlrDiaria DECIMAL(18,2),
  dataEntrega DATE,
  horaEntrega TIME,
  FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
  FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
  FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);

-- Tavolo Venditore
CREATE TABLE Vendedor (
  idVendedor INT PRIMARY KEY,
  nomeVendedor VARCHAR(15),
  sexoVendedor SMALLINT,
  estadoVendedor VARCHAR(40),
  idLocacao INT,
  FOREIGN KEY (idLocacao) REFERENCES Locacao(idLocacao)
);
