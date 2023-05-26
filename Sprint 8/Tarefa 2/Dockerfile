# Imagem base
FROM python:3.9

# Diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários
COPY requirements.txt .
COPY  task2.py .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Executar o script Python
CMD ["python", "task2.py"]

# Credenciais de acesso aws
ARG AKIA4JZ2XODUHTXM5D2G
ARG TY9eRcEID4tUyRYEs1k8TjYyeRnMPLK4wUHS7bbT

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
