FROM python:3.7.2-stretch

WORKDIR /app

COPY ./http-log-server/ /app

RUN pip install -r /app/requirements.txt --upgrade

EXPOSE 8001

ENTRYPOINT [ "python", "app.py" ]
