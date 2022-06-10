import threading
import time
from random import randrange

import click
from dotenv import load_dotenv

from models.gibberish_json_generator import GibberishHttpJson
from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)

load_dotenv()


class StressGenerator(object):
    def perform(self, **kwargs):
        threads = []
        num_threads = kwargs["n_threads"]

        for i in range(num_threads):
            threads.append(threading.Thread(
                target=self._kubernetes_job, name=i, kwargs=kwargs))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

    def _kubernetes_job(self, **kwargs):
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
                self._write_work(**kwargs)
            else:
                self._read_work(**kwargs)

            index += 1

    def _write_work(self, **kwargs):
        address = kwargs["address"]
        port = kwargs["port"]
        percentage_sampling = kwargs["percentage_sampling"]
        payload_size = kwargs["payload_size"]

        gibberish_http_json = GibberishHttpJson(payload_size, as_json=True)
        gibberish_content = gibberish_http_json.perform()

        simple_http_client_post = SimpleHttpLogClientPost(address, port)

        if (randrange(100) < percentage_sampling) and (threading.current_thread().name == '1'):
            self._calculate_latency_time_between_post_request(
                simple_http_client_post, gibberish_content)
            return

        simple_http_client_post.perform(gibberish_content)

    def _calculate_latency_time_between_post_request(self, simple_http_client_post: SimpleHttpLogClientPost, gibberish_content: list):
        st = time.time_ns()
        simple_http_client_post.perform(gibberish_content)
        et = time.time_ns()
        print(f"{et} {et - st}")

    def _read_work(self, **kwargs):
        address = kwargs["address"]
        port = kwargs["port"]
        percentage_sampling = kwargs["percentage_sampling"]
        qty_iteration = kwargs["qty_iteration"]

        simple_http_client_get = SimpleHttpLogClientGet(address, port)

        line_number = randrange(qty_iteration)

        if randrange(1, 100) < percentage_sampling:
            self._calculate_latency_time_between_get_request(
                simple_http_client_get, line_number)
            return

        simple_http_client_get.perform(line_number=line_number)

    def _calculate_latency_time_between_get_request(self, simple_http_client_get: SimpleHttpLogClientGet, line_number: int):
        st = time.time_ns()
        simple_http_client_get.perform(line_number=line_number)
        et = time.time_ns()
        print(f"{et} {et - st}")


@click.command()
@click.option("--address",             default="localhost", help="Server address")
@click.option("--port",                default=8000,        help="Server port")
@click.option("--payload_size",        default=10,          help="Set the payload size")
@click.option("--qty_iteration",       default=10000,       help="Set the key range to determine the volume")
@click.option("--read_rate",           default=10,          help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads",           default=10,          help="Set number of client threads")
@click.option("--thinking_time",       default=0.1,         help="Set thinking time between requests")
@click.option("--percentage_sampling", default=50,          help="Percentage of log in total")
@click.option("--duration",            default=1.5,           help="Duration in seconds")
def hello(**kwargs):
    StressGenerator().perform(**kwargs)


if __name__ == '__main__':
    hello()
