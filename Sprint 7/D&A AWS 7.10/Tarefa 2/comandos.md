Comandos que serão aplicados no exercício da tarefa 2 (em shell spark):

1- Ctrl+shift+P;
2- Dev Containers: Open folder in container;
3- Aguardar a abertura de uma nova janela do vscode;
4- Para entrar no shell, digitar "pyspark", sem as aspas. E, digitar os seguintes comandos:


arquivo_texto = sc.textFile("README.md")

contador_palavras = arquivo_texto.flatMap(lambda line: line.split(" ")) \
    .map(lambda palavra: (palavra, 1)) \
    .reduceByKey(lambda a, b: a + b)

for palavra, contador in contador_palavras.collect():
    print("{}: {}".format(palavra, contador))
