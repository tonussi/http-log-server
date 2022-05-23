import os

import click

from model.flask_app import FlaskApp


@click.command()
@click.option('--address', default="0.0.0.0", help='Server address')
@click.option('--port', default=8001, help='Server port')
@click.option('--buffer_size', default=1024, help='Requests buffer size')
@click.option('--tcp_onoff', default=False, help='Use mutex to each command or not')
def hello(address="0.0.0.0", port=8001, buffer_size=1024, tcp_onoff=False):
    """This program simulates the client making requests."""

    kwargs = {
        "address": address,
        "port": port,
        "tcp_onoff": tcp_onoff,
        "buffer_size": buffer_size
    }

    node_id = os.environ.get("NODE_ID", "node_not_set")

    flask_app = FlaskApp(node_id)
    click.echo(f"Starting {flask_app.app.name}")
    flask_app.app.run(host=address, port=port, debug=True)


if __name__ == '__main__':
    hello()
