FROM python:3.9

# Instalar dependências
RUN pip install boto3

# Copiar arquivos para o contêiner
COPY local_directory /app

# Configurar variáveis de ambiente
ENV AWS_ACCESS_KEY_ID your_access_key
ENV AWS_SECRET_ACCESS_KEY your_secret_key
ENV AWS_DEFAULT_REGION your_region

# Enviar arquivos para o bucket do S3
CMD python /app/upload_to_s3.py

# Comandos a executar:
# docker build -t s3-upload .
# docker run --rm -e AWS_ACCESS_KEY_ID=your_access_key -e AWS_SECRET_ACCESS_KEY=your_secret_key -e AWS_DEFAULT_REGION=your_region s3-upload


