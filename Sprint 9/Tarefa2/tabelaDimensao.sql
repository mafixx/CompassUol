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

-- Table Fatti Posizione
CREATE TABLE FatosLocacao (
  idLocacao INT PRIMARY KEY,
  idCliente INT,
  idCarro INT,
  idCombustivel INT,
  idVendedor INT,
  dataLocacao DATETIME,
  qtdDiaria INT,
  vlrDiaria DECIMAL(18,2),
  dataEntrega DATE,
  horaEntrega TIME,
  FOREIGN KEY (idCliente) REFERENCES DimCliente(idCliente),
  FOREIGN KEY (idCarro) REFERENCES DimCarro(idCarro),
  FOREIGN KEY (idCombustivel) REFERENCES DimCombustivel(idCombustivel),
  FOREIGN KEY (idVendedor) REFERENCES DimVendedor(idVendedor)
);


