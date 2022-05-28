import multiprocessing
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
from models.statistics import Statistics

load_dotenv()
mutex = threading.Lock()

os.environ["LATENCY_LOG"]="/tmp/logs/latency.log"


@click.command()
@click.option("--address", default="localhost", help="Server address")
@click.option("--port", default=8001, help="Server port")
@click.option("--duration", default=0.5, help="Set the duration of all the working in minutes")
@click.option("--payload_size", default=10, help="Set the payload size")
@click.option("--key_range", default=50, help="Set the key range to determine the volume")
@click.option("--read_rate", default=50, help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads", default=1, help="Set number of threads")
@click.option("--thinking_time", default=0.5, help="Set thinking time between requests")
@click.option("--log_frequency", default=1, help="Set log frequency")
@click.option("--mutex_onoff", default=False, help="Use mutex to each command or not")
def hello(address="localhost", port=8001, duration=0.5, payload_size=10, key_range=50, read_rate=50, n_threads=1, thinking_time=0.5, log_frequency=1, mutex_onoff=False):
    """This program simulates the client making requests."""

    # not working yet
    pod_id_index = os.environ.get("JOB_COMPLETION_INDEX", 0)

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
        "pod_id_index": pod_id_index
    }

    background.n = int(n_threads)

    # minutes from now
    timeout = time.time() + 60 * float(duration)

    while True:

        if randrange(100) < read_rate:
            time.sleep(int(thinking_time))
            _write_work(**kwargs)
        else:
            time.sleep(int(thinking_time))
            _read_work(**kwargs)

        if time.time() > timeout:
            break

    exit(0)


@background.task
def _write_work(**kwargs):
    address = kwargs["address"]
    port = kwargs["port"]
    key_range = kwargs["key_range"]
    mutex_onoff = kwargs["mutex_onoff"]
    thinking_time = kwargs["thinking_time"]
    pod_id_index = kwargs["pod_id_index"]
    log_frequency = kwargs["log_frequency"]

    # print("writing work")
    # print(f"{node_id} thinking...")

    time.sleep(int(thinking_time))

    gibberish_http_json = GibberishHttpJson(key_range, as_json=True)
    gibberish_content = gibberish_http_json.perform()
    simple_http_client_post = SimpleHttpLogClientPost(
        address, port, pod_id_index)

    if mutex_onoff:
        with mutex:
            simple_http_client_post.perform(gibberish_content)
            # print(simple_http_client_post.perform(gibberish_content))
    else:
        simple_http_client_post.perform(gibberish_content)
        # print(simple_http_client_post.perform(gibberish_content))

    Statistics(pod_id_index, log_frequency).perform()


@background.task
def _read_work(**kwargs):
    address = kwargs["address"]
    port = kwargs["port"]
    key_range = kwargs["key_range"]
    mutex_onoff = kwargs["mutex_onoff"]
    thinking_time = kwargs["thinking_time"]
    pod_id_index = kwargs["pod_id_index"]
    log_frequency = kwargs["log_frequency"]

    # print("reading work")
    # print(f"{node_id} thinking...")

    time.sleep(int(thinking_time))

    simple_http_client_get = SimpleHttpLogClientGet(
        address, port, pod_id_index)

    if mutex_onoff:
        with mutex:
            for line in range(key_range):
                simple_http_client_get.perform(line_number=line)
                # print(simple_http_client_get.perform(line_number=line))
    else:
        for line in range(key_range):
            simple_http_client_get.perform(line_number=line)
            # print(simple_http_client_get.perform(line_number=line))

    Statistics(pod_id_index, log_frequency).perform()


if __name__ == '__main__':
    hello()
