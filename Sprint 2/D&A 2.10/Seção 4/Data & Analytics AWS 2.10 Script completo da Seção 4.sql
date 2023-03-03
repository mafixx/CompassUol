-- #E8 Apresente a query para listar o código e o nome do vendedor com maior 
-- número de vendas (contagem), e que estas vendas estejam 
-- com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select cdvdd, nmvdd
	from tbvendedor as v
order by (select count(*) 
	from tbvendas as vn 
	where vn.cdvdd = v.cdvdd) desc
limit 1


-- #E9 Apresente a query para listar o código e nome do produto 
-- mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
-- e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser cdpro e nmpro.

SELECT vn.cdpro, vn.nmpro, 
COUNT(vn.status = 'Concluído') qtd_vendas
FROM tbvendas vn
WHERE vn.status = 'Concluído' AND vn.dtven BETWEEN '2014-02-02' AND '2018-02-03' 
--AND vn.cdpro = 1
GROUP BY vn.nmpro
LIMIT 1

SELECT vn.cdpro, vn.nmpro--, (SELECT COUNT(*) FROM tbvendas v WHERE v.cdpro = vn.cdpro) qtd, dtven
FROM tbvendas vn
WHERE vn.status = 'Concluído' AND vn.dtven BETWEEN '2014-02-02' AND '2018-02-03' 
--AND vn.cdpro = 1
GROUP BY vn.cdpro
ORDER BY (SELECT COUNT(*) FROM tbvendas v WHERE v.cdpro = vn.cdpro) DESC
LIMIT 1


-- #E10 A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas 
-- armazenadas na base de dados com status concluído.
-- As colunas presentes no resultado devem ser vendedor, 
-- valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

SELECT vd.nmvdd vendedor, SUM(vn.qtd * vn.vrunt) valor_total_vendas, 
ROUND(SUM(vn.qtd * vn.vrunt) * vd.perccomissao / 100, 2) comissao--, 
--vd.perccomissao
FROM tbvendas vn
INNER JOIN tbvendedor vd ON vd.cdvdd = vn.cdvdd
WHERE vn.status = 'Concluído'
GROUP BY vd.cdvdd
ORDER BY comissao DESC


-- #E11 Apresente a query para listar o código e nome cliente 
-- com maior gasto na loja. As colunas presentes no resultado 
-- devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

SELECT cdcli, nmcli, SUM(vrunt * qtd) gasto
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY cdcli
ORDER BY gasto DESC
LIMIT 1


-- #E12 Apresente a query para listar código, nome e data de nascimento 
-- dos dependentes do vendedor com menor valor total bruto 
-- em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

-- Observação: Apenas vendas com status concluído.

SELECT d.cddep, d.nmdep, d.dtnasc, SUM(v.qtd * v.vrunt) valor_total_vendas
FROM tbvendas v 
INNER JOIN tbdependente d ON d.cdvdd = v.cdvdd
WHERE v.status = 'Concluído' --AND v.cdvdd = 9
GROUP BY v.cdvdd
ORDER BY valor_total_vendas ASC
LIMIT 1 --BY valor_total_vendas --DESC


-- #E13 Apresente a query para listar os 10 produtos menos vendidos pelos canais 
-- de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  
-- As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT cdpro, nmcanalvendas, nmpro, SUM(qtd) quantidade_vendas
FROM tbvendas
WHERE status = 'Concluído' --AND nmcanalvendas = 'Ecommerce' --AND nmcanalvendas = 'Matriz'
GROUP BY cdpro, nmcanalvendas
ORDER BY quantidade_vendas ASC


-- #E14 Apresente a query para listar o gasto médio por estado da federação. 
-- As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar 
-- a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

-- Observação: Apenas vendas com status concluído.

SELECT estado, ROUND(SUM(ROUND(vrunt, 2) * ROUND(qtd, 2)) / ROUND(COUNT(*), 2), 2) gastomedio
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado
ORDER BY ROUND(gastomedio, 2) DESC

-- #E15 Apresente a query para listar os códigos das vendas identificadas como deletadas. 
-- Apresente o resultado em ordem crescente.

SELECT cdven
FROM tbvendas
WHERE deletado = 1
ORDER BY cdven ASC

-- #E16 Apresente a query para listar a quantidade média vendida de cada produto agrupado 
-- por estado da federação. As colunas presentes no resultado devem ser estado e 
-- nmprod e quantidade_media. Considere arredondar o valor da coluna 
-- quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

-- Obs: Somente vendas concluídas.

SELECT estado, nmpro, ROUND(ROUND(SUM(qtd), 4) / ROUND(COUNT(*), 4), 4) quantidade_media
FROM tbvendas
WHERE status = 'Concluído' --AND deletado = 0
GROUP BY estado, nmpro
ORDER BY estado, nmpro