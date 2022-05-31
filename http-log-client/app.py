import threading
import time
from random import randrange

import background
import click
from dotenv import load_dotenv

from models.gibberish_json_generator import GibberishHttpJson
from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)

from time import sleep, perf_counter
import threading
load_dotenv()


@click.command()
@click.option("--address", default="localhost", help="Server address")
@click.option("--port", default=8000, help="Server port")
@click.option("--payload_size", default=2, help="Set the payload size")
@click.option("--qty_iteration", default=50, help="Set the key range to determine the volume")
@click.option("--read_rate", default=50, help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads", default=1, help="Set number of threads")
@click.option("--thinking_time", default=0.5, help="Set thinking time between requests")
@click.option("--log_frequency", default=0.1, help="Set log frequency")
@click.option("--percentage_sampling", default=80, help="Use mutex to each command or not")
def hello(**kwargs):
    threads = []
    num_threads = kwargs["n_threads"]

    for i in range(num_threads):
        threads.append(threading.Thread(
            target=_kubernetes_job, name=i, kwargs=kwargs))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def _kubernetes_job(**kwargs):
    qty_iteration = kwargs["qty_iteration"]
    read_rate = kwargs["read_rate"]
    thinking_time = kwargs["thinking_time"]

    for _ in range(qty_iteration):
        if randrange(100) < read_rate:
            time.sleep(int(thinking_time))
            _write_work(**kwargs)
        else:
            time.sleep(int(thinking_time))
            _read_work(**kwargs)


def _write_work(**kwargs):
    address = kwargs["address"]
    port = kwargs["port"]
    payload_size = kwargs["payload_size"]
    thinking_time = kwargs["thinking_time"]
    percentage_sampling = kwargs["percentage_sampling"]

    time.sleep(int(thinking_time))

    gibberish_http_json = GibberishHttpJson(payload_size, as_json=True)
    gibberish_content = gibberish_http_json.perform()
    simple_http_client_post = SimpleHttpLogClientPost(address, port)

    if (randrange(100) < percentage_sampling) and (threading.current_thread().name == '1'):
        time_between_post_request(simple_http_client_post, gibberish_content)

    return simple_http_client_post.perform(gibberish_content)


def time_between_post_request(simple_http_client_post: SimpleHttpLogClientPost, gibberish_content: list):
    st = perf_counter()
    simple_http_client_post.perform(gibberish_content)
    et = perf_counter()
    print(f"{et} {et - st}")


def _read_work(**kwargs):
    address = kwargs["address"]
    port = kwargs["port"]
    thinking_time = kwargs["thinking_time"]
    percentage_sampling = kwargs["percentage_sampling"]
    qty_iteration = kwargs["qty_iteration"]

    time.sleep(int(thinking_time))

    simple_http_client_get = SimpleHttpLogClientGet(address, port)

    line_number = randrange(qty_iteration)

    if threading.get_ident() != 1:
        return simple_http_client_get.perform(line_number=line_number)

    if randrange(100) < percentage_sampling:
        return time_between_get_request(simple_http_client_get, line_number)

    return simple_http_client_get.perform(line_number=line_number)


def time_between_get_request(simple_http_client_get: SimpleHttpLogClientGet, line_number: int):
    st = time.time()
    simple_http_client_get.perform(line_number=line_number)
    et = time.time()
    print(f"{et} {et - st}")


if __name__ == '__main__':
    hello()
