-- #E8 Apresente a query para listar o código e o nome do vendedor com maior 
-- número de vendas (contagem), e que estas vendas estejam 
-- com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select cdvdd, nmvdd
	from tbvendedor as v
order by (select count(*) 
	from tbvendas as vn 
	where vn.cdvdd = v.cdvdd) desc
limit 1