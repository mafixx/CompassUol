#Query1
CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.bank (
  nome STRING,
  sexo STRING,
  total INT,
  ano INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION "s3://phrb-bucket/dados/" 

#Query2
select nome from meubanco.bank where ano = 1999 order by total limit 15;

#Query3
SELECT nome, sexo, SUM(total) AS total, ano
FROM (
  SELECT nome, sexo, total, ano,
         ROW_NUMBER() OVER (PARTITION BY CAST(ano/10 AS INT) ORDER BY total DESC) AS num_row
  FROM bank
  WHERE ano >= 1950 AND ano % 10 = 0
) AS subquery
WHERE num_row <= 3
GROUP BY nome, sexo, ano
ORDER BY ano, total DESC;
