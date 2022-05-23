import os

import click

from model.flask_app import FlaskApp
from model.tcp_app import TcpApp


@click.command()
@click.option('--address', default="0.0.0.0", help='Server address')
@click.option('--port', default=8001, help='Server port')
@click.option('--buffer_size', default=1024, help='Requests buffer size')
@click.option('--tcp_onoff', default=False, help='Use mutex to each command or not')
def hello(address="0.0.0.0", port=8001, buffer_size=1024, tcp_onoff=False):
    """This program simulates the client making requests."""

    node_id = os.environ.get("NODE_ID", "node_not_set")
    kwargs = {
        "address": address,
        "port": port,
        "tcp_onoff": tcp_onoff,
        "buffer_size": buffer_size,
        "node_id": node_id
    }

    if tcp_onoff:
        click.echo("TcpApp")
        flask_app = TcpApp(**kwargs)
        flask_app.perform()
    else:
        click.echo("FlaskApp")
        flask_app = FlaskApp(**kwargs)
        flask_app.perform()


if __name__ == '__main__':
    hello()
