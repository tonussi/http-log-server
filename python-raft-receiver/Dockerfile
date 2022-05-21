FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8001

ENTRYPOINT ["python", "app.py"]
