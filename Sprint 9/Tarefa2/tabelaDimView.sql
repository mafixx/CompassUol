-- Creare la vista per la dimensione Cliente
CREATE VIEW vw_DimCliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

-- Creare la vista per la dimensione Carro
CREATE VIEW vw_DimCarro AS
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM Carro;

-- Creare la vista per la dimensione Combustivel
CREATE VIEW vw_DimCombustivel AS
SELECT idCombustivel, tipoCombustivel
FROM Combustivel;

-- Crea la vista per la dimensione Vendedor 
CREATE VIEW vw_DimVendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor;

-- Crea la vista per la tabella dei fatti Locacao
CREATE VIEW vw_Locacao AS
SELECT l.idLocacao, c.idCliente, ca.idCarro, cb.idCombustivel, v.idVendedor,
       l.dataLocacao, l.horaLocacao, l.qtdDiaria, l.vlrDiaria, l.dataEntrega, l.horaEntrega
FROM Locacao l
JOIN Cliente c ON l.idCliente = c.idCliente
JOIN Carro ca ON l.idCarro = ca.idCarro
JOIN Combustivel cb ON l.idCombustivel = cb.idCombustivel
JOIN Vendedor v ON l.idLocacao = v.idLocacao;