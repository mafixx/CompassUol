# Exercício 1
# Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código carguru.py. Após, execute um container a partir da imagem criada.
# Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container.
# É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.


# Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Seguem as instruções.

# -- Criar novo script Python que implementa o algoritmo a seguir:
# 1 - Receber uma string via input
# 2 - Gerar o hash da string por meio do algoritmo SHA-1
# 3 - Imprimir o hash em tela, utilizando o método hexdigest
# 4 - Retornar ao passo 1

# -- Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente

# --  Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento

# -- Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.



### Criando a imagem Docker chamada mascarar-dados:

# Use uma imagem do Python como base
FROM python:3.9-slim-buster

# Copie o script Python para dentro do container
COPY script.py /

# Instale as dependências necessárias
#RUN pip install hashlib

# Defina o comando que será executado quando o container for iniciado
CMD ["python", "/script.py"]