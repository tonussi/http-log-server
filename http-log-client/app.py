import os
import click
from dotenv import load_dotenv
from models.simple_http_log_client import SimpleHttpLogClientPost, SimpleHttpLogClientGet
from models.gibberish_json_generator import GibberishHttpJson

load_dotenv()


@click.command()
@click.option("--address",       default="localhost", help="Server address")
@click.option("--port",          default=8000,        help="Server port")
@click.option("--duration",      default=60,          help="Set the duration of all the working")
@click.option("--payload_size",  default=128,         help="Set the payload size")
@click.option("--key_range",     default=100000,      help="Set the key range to determine the volume")
@click.option("--read_rate",     default=128,         help="Set the reading rate")
@click.option("--n_threads",     default=4,           help="Set number of threads")
@click.option("--thinking_time", default=10,          help="Set thinking time between requests")
@click.option("--log_frequency", default=30,          help="Set log frequency")
@click.option("--buffer_size",   default=1024,        help="Set buffer size for each request")
@click.option("--mutex_onoff",   default=False,       help="Use mutex to each command or not")
def hello(
        address="localhost",
        port=8000,
        duration=60,
        payload_size=128,
        key_range=100000,
        read_rate=128,
        n_threads=5,
        thinking_time=10,
        log_frequency=30,
        buffer_size=1024,
        mutex_onoff=False
    ):
    """This program simulates the client making requests."""

    click.echo(
        {
            "address"       : address,
            "port"          : port,
            "mutex_onoff"   : mutex_onoff,
            "duration"      : duration,
            "payload_size"  : payload_size,
            "key_range"     : key_range,
            "read_rate"     : read_rate,
            "n_threads"     : n_threads,
            "thinking_time" : thinking_time,
            "log_frequency" : log_frequency,
            "buffer_size"   : buffer_size
        }
    )

    click.echo(
        os.environ.get("NODE_ID", "node_not_set")
    )

    CONTENT_SIZE = 50

    gibberish_http_json = GibberishHttpJson(CONTENT_SIZE, as_json=True)
    gibberish_content = gibberish_http_json.perform()

    simple_http_client_post = SimpleHttpLogClientPost(
        address,
        port,
        duration,
        payload_size,
        key_range,
        read_rate,
        n_threads,
        thinking_time,
        log_frequency,
        buffer_size,
        mutex_onoff
    )
    click.echo(simple_http_client_post.perform(gibberish_content))

    simple_http_client_get = SimpleHttpLogClientGet(
        address,
        port,
        duration,
        payload_size,
        key_range,
        read_rate,
        n_threads,
        thinking_time,
        log_frequency,
        buffer_size,
        mutex_onoff
    )
    for line in range(CONTENT_SIZE):
        click.echo(simple_http_client_get.perform(line_number=line))

    exit(0)


if __name__ == '__main__':
    hello()
