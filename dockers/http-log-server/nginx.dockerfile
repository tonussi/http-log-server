FROM nginx:1.21.6-alpine

RUN ls /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf

ARG FLASK_BACKEND_IP

ENV IP_BACKEND_DOCKER_HTTP_LOG_SERVER ${FLASK_BACKEND_IP}

# RUN echo $FLASK_BACKEND_IP

RUN echo $IP_BACKEND_DOCKER_HTTP_LOG_SERVER

# Replace with our own nginx.conf

ENV NGINX_CONF "server { \
    listen 80; \
    location / { \
        include uwsgi_params; \
        uwsgi_pass ${IP_BACKEND_DOCKER_HTTP_LOG_SERVER}:8080; \
    } \
}"

RUN echo ${NGINX_CONF} > /etc/nginx/conf.d/nginx.conf
RUN cat /etc/nginx/conf.d/nginx.conf
