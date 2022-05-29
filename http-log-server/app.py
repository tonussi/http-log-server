import os

import click

from models.flask_app import FlaskApp
from models.custom_http_app import CustomHttpApp


os.environ["FLASK_APP"]="api.py"
os.environ["FLASK_ENV"]="production"
os.environ["SOURCE_DB"]="/tmp/logs/operations.log"
os.environ["BACKUPS_DIR"]="/tmp/logs/replicas"
os.environ["THROUGHPUT_LOG"]="/tmp/logs/throughput.log"



@click.command()
@click.option('--address', default="0.0.0.0", help='Server address')
@click.option('--port', default=8001, help='Server port')
@click.option('--tcp_onoff', default=False, help='Use mutex to each command or not')
def hello(address="0.0.0.0", port=8001, tcp_onoff=False):
    """This program simulates the client making requests."""

    node_id = os.environ.get("NODE_ID", "node_not_set")
    kwargs = {
        "address": address,
        "port": port,
        "tcp_onoff": tcp_onoff,
        "node_id": node_id
    }

    if tcp_onoff:
        click.echo("CustomHttpApp")
        flask_app = CustomHttpApp(**kwargs)
        flask_app.perform()
    else:
        click.echo("FlaskApp")
        flask_app = FlaskApp(**kwargs)
        flask_app.perform()


if __name__ == '__main__':
    hello()
