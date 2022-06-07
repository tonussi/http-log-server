FROM python:3.7.2-stretch

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8001

ENTRYPOINT ["python", "app.py"]
