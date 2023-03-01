-- #E1 Apresente a query para listar todos os livros publicados 
-- após 2014. Ordenar pela coluna cod, em ordem crescente, 
-- as linhas.  Atenção às colunas esperadas no resultado final: 
-- cod, titulo, autor, editora, valor, publicacao, edicao, idioma

SELECT *
FROM livro
WHERE publicacao >= '2015-01-01'
ORDER BY cod ASC 


-- #E2 Apresente a query para listar os 10 livros mais caros. 
-- Ordenar as linhas pela coluna valor, em ordem decrescente.  
-- Atenção às colunas esperadas no resultado final:  titulo, valor.

SELECT titulo, valor
from livro 
order by valor DESC 
limit 10


-- #E3 Apresente a query para listar as 5 editoras com mais livros 
-- na biblioteca. O resultado deve conter apenas as colunas 
-- quantidade, nome, estado e cidade. Ordenar as linhas pela 
-- coluna que representa a quantidade de livros em ordem decrescente.

select 
	count (liv.titulo) as quantidade,
	ed.nome,
	estado,
	cidade
from livro as liv
left join editora as ed
	on liv.editora = ed.codeditora
left join endereco as adress
	on ed.endereco = adress.codendereco 
group by ed.codeditora
order by quantidade desc


-- #E4 Apresente a query para listar a quantidade de livros 
-- publicada por cada autor. Ordenar as linhas 
-- pela coluna nome (autor), em ordem crescente. Além desta, 
-- apresentar as colunas codautor, nascimento e quantidade 
-- (total de livros de sua autoria).

select * from livro 

select * from autor

select 
	au.nome,
	au.codautor,
	au.nascimento,
	count (liv.titulo) as quantidade
from autor as au
left join livro as liv
	on au.codautor = liv.autor
group by au.nome
ORDER BY au.nome asc
--select replace ('ÀVILA', 'ÀVILA', 'AVILA') = 'AVILA'


-- #E5 Apresente a query para listar o nome dos autores que 
-- publicaram livros através de editoras NÃO situadas na região 
-- sul do Brasil. Ordene o resultado pela coluna nome, 
-- em ordem crescente. Não podem haver nomes repetidos em seu retorno.

Select distinct au.nome
from autor as au
    left join livro as liv
    on au.codautor = liv.autor
    left join editora as ed
    on liv.editora=ed.codeditora
    left join endereco as adress
    on ed.endereco = adress.codendereco
where adress.estado not in ('PARANÁ','RIO GRANDE DO SUL', 'SANTA CATARINA')
order by au.nome asc


-- #E6 Apresente a query para listar o autor com maior 
-- número de livros publicados. 
-- O resultado deve conter apenas as colunas codautor, nome, 
-- quantidade_publicacoes.

SELECT * from autor

select codautor, nome,
	(select count(*)
	from livro l where l.autor = a.codautor)
quantidade_publicacoes
from autor a
order by quantidade_publicacoes desc
limit 1


-- #E7 Apresente a query para listar o nome dos autores com 
-- nenhuma publicação. Apresentá-los em ordem crescente.

SELECT nome
FROM autor
WHERE 
	(SELECT COUNT(*) 
	FROM livro l 
	INNER JOIN autor a 
	ON a.codautor = l.autor 
	WHERE a.codautor = autor.codautor) = 0
ORDER BY nome;









