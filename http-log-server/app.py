import os

import click

from models.custom_http_app import HttpApp


os.environ["FLASK_APP"] = "api.py"
os.environ["FLASK_ENV"] = "production"
os.environ["SOURCE_DB"] = "/tmp/logs/operations.log"
os.environ["BACKUPS_DIR"] = "/tmp/logs/replicas"
os.environ["THROUGHPUT_LOG"] = "/tmp/logs/throughput.log"


@click.command()
@click.option('--address', default="0.0.0.0", help='Server address')
@click.option('--port', default=8001, help='Server port')
def start_server(**kwargs):
    HttpApp(**kwargs)


if __name__ == '__main__':
    start_server()
