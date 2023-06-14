### Tarefa 4:

> Criação do banco de dados com camada refined com o csv em parquet e o json(tmdb) em parquet.
> Para posterior criação de views, seria necessária a seguinte demanda:

~~~sql
CREATE OR REPLACE VIEW view_movies AS
SELECT c.id, c.titulooriginal AS titulooriginal_csv, c.anolancamento, t.titulopincipal AS tituloprincipal_tmdb, t.notamedia
FROM csvtoparquet c, tmdb2 t;
~~~

![Tables criadas](img/tabelasparquetrefinadas.png)