import os

import click

from models.custom_http_app import CustomHttpApp


@click.command()
@click.option('--address', default="0.0.0.0", help='Server address')
@click.option('--port', default=8001, help='Server port')
def hello(**kwargs):
    http_handler_app = CustomHttpApp(**kwargs)
    http_handler_app.perform()

if __name__ == '__main__':
    hello()
