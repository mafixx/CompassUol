 #! /bin/sh
docker build -t carguru-image -f Dockerfile .
docker rm carguru
docker run --name carguru -it carguru-image