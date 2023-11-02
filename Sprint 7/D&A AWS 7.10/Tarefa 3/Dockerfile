FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "boto.py" ]

ARG ACCESSKEYHERE
ARG SECRETKEYHERE

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

# Para a construção da imagem: docker build -t boto .
# Para rodar a imagem: docker run boto
