FROM python:3.7.2-stretch

WORKDIR /app

COPY ./http-log-client/ /app

RUN pip install -r requirements.txt --upgrade

ENTRYPOINT [ "python", "app.py" ]
