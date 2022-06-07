import multiprocessing
import threading
import time
from random import randrange

import click
from dotenv import load_dotenv

from models.gibberish_json_generator import GibberishHttpJson
from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)

load_dotenv()


@click.command()
@click.option("--address", default="localhost", help="Server address")
@click.option("--port", default=8000, help="Server port")
@click.option("--payload_size", default=1, help="Set the payload size")
@click.option("--qty_iteration", default=1000000, help="Set the key range to determine the volume")
@click.option("--read_rate", default=50, help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads", default=30, help="Set number of client threads")
@click.option("--thinking_time", default=0.2, help="Set thinking time between requests default is 200ms")
@click.option("--percentage_sampling", default=95, help="Percentage of log in total")
@click.option("--duration", default=1.5, help="Duration in seconds")
def hello(**kwargs):
    threads = []
    num_threads = kwargs["n_threads"]
    payload_size = kwargs["payload_size"]

    gibberish_http_json = GibberishHttpJson(payload_size, as_json=True)
    gibberish_content = gibberish_http_json.perform()
    kwargs["gibberish_content"] = gibberish_content

    for i in range(num_threads):
        threads.append(threading.Thread(
            target=_kubernetes_job, name=i, kwargs=kwargs))

    kwargs["threads"] = threads

    for t in threads:
        t.start()


def _kubernetes_job(**kwargs):
    qty_iteration = kwargs["qty_iteration"]
    read_rate = kwargs["read_rate"]
    thinking_time = kwargs["thinking_time"]
    duration = kwargs["duration"]

    timeout = time.time() + 60*duration
    index = 0

    while index < qty_iteration:
        if time.time() > timeout:
            break

        time.sleep(thinking_time)

        if randrange(1, 100) < read_rate:
            _write_work(**kwargs)
        else:
            _read_work(**kwargs)

        index += 1


def _write_work(**kwargs):
    address = kwargs["address"]
    port = kwargs["port"]
    gibberish_content = kwargs["gibberish_content"]
    percentage_sampling = kwargs["percentage_sampling"]

    simple_http_client_post = SimpleHttpLogClientPost(address, port)

    try:
        if (randrange(100) < percentage_sampling) and (threading.current_thread().name == '1'):
            calculate_latency_time_between_post_request(
                simple_http_client_post, gibberish_content)
            return

        simple_http_client_post.perform(gibberish_content)
    except:
        pass


def calculate_latency_time_between_post_request(simple_http_client_post: SimpleHttpLogClientPost, gibberish_content: list):
    st = time.time_ns()
    simple_http_client_post.perform(gibberish_content)
    et = time.time_ns()
    print(f"{et} {et - st}")


def _read_work(**kwargs):
    address = kwargs["address"]
    port = kwargs["port"]
    percentage_sampling = kwargs["percentage_sampling"]
    qty_iteration = kwargs["qty_iteration"]

    simple_http_client_get = SimpleHttpLogClientGet(address, port)

    line_number = randrange(qty_iteration)

    try:
        if (randrange(1, 100) < percentage_sampling) and (threading.current_thread().name == '1'):
            calculate_latency_time_between_get_request(
                simple_http_client_get, line_number)
            return

        simple_http_client_get.perform(line_number=line_number)
    except:
        pass


def calculate_latency_time_between_get_request(simple_http_client_get: SimpleHttpLogClientGet, line_number: int):
    st = time.time_ns()
    simple_http_client_get.perform(line_number=line_number)
    et = time.time_ns()
    print(f"{et} {et - st}")


if __name__ == '__main__':
    hello()
