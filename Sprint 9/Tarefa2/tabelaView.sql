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
