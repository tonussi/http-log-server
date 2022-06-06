#!/usr/bin/env sh
DOCKERHUB_USER_NAME=lptonussi

docker build -t $DOCKERHUB_USER_NAME/public:http-log-client -f dockers/http-log-client/Dockerfile .
docker push $DOCKERHUB_USER_NAME/public:http-log-client

docker build -t $DOCKERHUB_USER_NAME/public:http-log-server -f dockers/http-log-server/Dockerfile .
docker push $DOCKERHUB_USER_NAME/public:http-log-server

docker run -p 8000:5000 --name http-log-server $DOCKERHUB_USER_NAME/public:http-log-server
export IP_BACKEND_DOCKER_HTTP_LOG_SERVER=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' http-log-server);
echo $IP_BACKEND_DOCKER_HTTP_LOG_SERVER

# docker build -t tonussi/http-log-server-nginx --build-arg FLASK_BACKEND_IP=${IP_BACKEND_DOCKER_HTTP_LOG_SERVER} -f dockers/http-log-server/nginx.dockerfile .
# docker run -p 5000:80 --name http-log-server-nginx tonussi/http-log-server-nginx

export IP_NGINX_DOCKER_HTTP_LOG_SERVER=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' http-log-server-nginx);
echo $IP_NGINX_DOCKER_HTTP_LOG_SERVER

# docker run --env IP_NGINX_DOCKER_HTTP_LOG_SERVER=${IP_NGINX_DOCKER_HTTP_LOG_SERVER} --env NGINX_FLASK_PORT=5000 --name http-log-client tonussi/http-log-client
docker run --name http-log-client $DOCKERHUB_USER_NAME/public:http-log-client

PID=$(docker inspect --format '{{.State.Pid}}' nginx-http-log-client)

kubectl patch service http-log-server -p '{"spec": {"type": "LoadBalancer", "externalIPs":["192.168.0.9"]}}'
