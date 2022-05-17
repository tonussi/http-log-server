FROM python:3.7.2-stretch

WORKDIR /app

ADD ./http-log-server/ /app

RUN pip install -r /app/requirements.txt

EXPOSE 8001

ENTRYPOINT [ "python", "app.py" ]
