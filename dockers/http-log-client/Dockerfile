FROM python:3.7.2-stretch

WORKDIR /app

ADD ./http-log-client/ /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]
