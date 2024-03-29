# Tarefa 2:
### Identificar as tabelas de dimensão:
> - Cliente
> - Carro
> - Combustivel
> - Vendedor

### Criando as tabelas de dimensão e visualização correspondentes:
~~~sql
-- Criando a visualização da dimensão Cliente
CREATE VIEW vw_DimCliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

-- Criando a visualização da dimensão Carro
CREATE VIEW vw_DimCarro AS
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM Carro;

-- Criando a visualização da dimensão Combustivel
CREATE VIEW vw_DimCombustivel AS
SELECT idCombustivel, tipoCombustivel
FROM Combustivel;

-- Criando a visualização da dimensão Vendedor 
CREATE VIEW vw_DimVendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor;

-- Criando a visualização da tabela Locacao
CREATE VIEW vw_Locacao AS
SELECT l.idLocacao, c.idCliente, ca.idCarro, cb.idCombustivel, v.idVendedor,
       l.dataLocacao, l.horaLocacao, l.qtdDiaria, l.vlrDiaria, l.dataEntrega, l.horaEntrega
FROM Locacao l
JOIN Cliente c ON l.idCliente = c.idCliente
JOIN Carro ca ON l.idCarro = ca.idCarro
JOIN Combustivel cb ON l.idCombustivel = cb.idCombustivel
JOIN Vendedor v ON l.idLocacao = v.idLocacao;
~~~


# Output

![Modelo Dimensional](img/concessionaria%20ER%20Diagram.png)

![Execução](img/printGeral.png)