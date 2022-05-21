import os

import click

from model.flask_app import FlaskApp


@click.command()
@click.option('--address',     default="0.0.0.0",             help='Server address')
@click.option('--port',        default=8001,                  help='Server port')
@click.option('--log_path',    default="/tmp/throughput.log", help='Path to log the throughput')
@click.option('--buffer_size', default=2048,                  help='Requests buffer size')
@click.option('--key_range',   default=100000,                help='Key range')
@click.option('--value_size',  default=1024,                  help='Base value size for pre-population')
@click.option('--mutex_onoff', default=False,                 help='Use mutex to each command or not')
def hello(address="0.0.0.0", port=8001, log_path="/tmp/throughput.log", buffer_size=2048, key_range=100000, value_size=1024, mutex_onoff=False):
    """This program simulates the client making requests."""

    click.echo(
        {
            "address": address,
            "port": port,
            "log_path": log_path,
            "buffer_size": buffer_size,
            "key_range": key_range,
            "value_size": value_size,
            "mutex_onoff": mutex_onoff
        }
    )

    node_id = os.environ.get("NODE_ID", "node_not_set")
    flask_app = FlaskApp(node_id)
    click.echo(f"Starting {flask_app.app.name}")
    flask_app.app.run(host=address, port=port, debug=True)


if __name__ == '__main__':
    hello()
