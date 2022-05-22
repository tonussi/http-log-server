import os
import threading
import time
from random import randrange

import background
import click
from dotenv import load_dotenv

from models.gibberish_json_generator import GibberishHttpJson
from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)

load_dotenv()
mutex = threading.Lock()


@click.command()
@click.option("--address", default="localhost", help="Server address")
@click.option("--port", default=8001, help="Server port")
@click.option("--duration", default=2, help="Set the duration of all the working in minutes")
@click.option("--payload_size", default=10, help="Set the payload size")
@click.option("--key_range", default=50, help="Set the key range to determine the volume")
@click.option("--read_rate", default=50, help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads", default=2, help="Set number of threads")
@click.option("--thinking_time", default=1, help="Set thinking time between requests")
@click.option("--log_frequency", default=30, help="Set log frequency")
@click.option("--buffer_size", default=1024, help="Set buffer size for each request")
@click.option("--mutex_onoff", default=False, help="Use mutex to each command or not")
def hello(
    address="localhost",
    port=8001,
    duration=5,
    payload_size=50,
    key_range=50,
    read_rate=50,
    n_threads=4,
    thinking_time=1,
    log_frequency=30,
    buffer_size=1024,
    mutex_onoff=False
):
    """This program simulates the client making requests."""

    node_id = os.environ.get("NODE_ID", "node_not_set")
    click.echo(node_id)

    kwargs = {
        "address": address,
        "port": port,
        "mutex_onoff": mutex_onoff,
        "duration": duration,
        "payload_size": payload_size,
        "key_range": key_range,
        "read_rate": read_rate,
        "n_threads": n_threads,
        "thinking_time": thinking_time,
        "log_frequency": log_frequency,
        "buffer_size": buffer_size,
        "node_id": node_id
    }

    background.n = int(n_threads)

    # minutes from now
    timeout = time.time() + 60 * int(duration)

    while True:

        if randrange(100) < read_rate:
            read_work(**kwargs)
        else:
            time.sleep(int(thinking_time))
            write_work(**kwargs)

        if time.time() > timeout:
            break

    exit(0)


@background.task
def write_work(**kwargs):

    address = kwargs["address"]
    port = kwargs["port"]
    key_range = kwargs["key_range"]
    mutex_onoff = kwargs["mutex_onoff"]
    thinking_time = kwargs["thinking_time"]
    node_id = kwargs["node_id"]

    click.echo("writing work")
    click.echo(f"{node_id} thinking...")

    time.sleep(int(thinking_time))

    gibberish_http_json = GibberishHttpJson(key_range, as_json=True)
    gibberish_content = gibberish_http_json.perform()
    simple_http_client_post = SimpleHttpLogClientPost(address, port, node_id)

    if mutex_onoff:
        with mutex:
            click.echo(simple_http_client_post.perform(gibberish_content))
    else:
        click.echo(simple_http_client_post.perform(gibberish_content))


@background.task
def read_work(**kwargs):

    address = kwargs["address"]
    port = kwargs["port"]
    key_range = kwargs["key_range"]
    mutex_onoff = kwargs["mutex_onoff"]
    thinking_time = kwargs["thinking_time"]
    node_id = kwargs["node_id"]

    click.echo("reading work")
    click.echo(f"{node_id} thinking...")

    time.sleep(int(thinking_time))

    simple_http_client_get = SimpleHttpLogClientGet(address, port, node_id)

    if mutex_onoff:
        with mutex:
            for line in range(key_range):
                click.echo(simple_http_client_get.perform(line_number=line))
    else:
        for line in range(key_range):
            click.echo(simple_http_client_get.perform(line_number=line))


if __name__ == '__main__':
    hello()
