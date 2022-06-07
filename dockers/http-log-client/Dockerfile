FROM python:3.7.2-stretch

WORKDIR /app

COPY ./http-log-client/ /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]
