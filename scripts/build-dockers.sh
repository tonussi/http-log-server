#!/usr/bin/env sh
DOCKERHUB_USER_NAME=lptonussi

docker build -t $DOCKERHUB_USER_NAME/public:http-log-client -f dockers/http-log-client/Dockerfile .
docker build -t $DOCKERHUB_USER_NAME/public:http-log-server -f dockers/http-log-server/Dockerfile .

docker push $DOCKERHUB_USER_NAME/public:http-log-server
docker push $DOCKERHUB_USER_NAME/public:http-log-client
