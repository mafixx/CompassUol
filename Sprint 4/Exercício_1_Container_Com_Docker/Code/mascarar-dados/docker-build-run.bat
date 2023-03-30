docker build -t mascarar-dados-image -f Dockerfile .
docker rm mascarar-dados
docker run --name mascarar-dados -it mascarar-dados-image