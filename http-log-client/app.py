from multiprocessing import Lock
import threading
import time
from random import randrange

import click
from dotenv import load_dotenv

from models.gibberish_json_generator import GibberishHttpJson
from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)

load_dotenv()

printf_mutex = Lock()

class StressGenerator(object):
    def perform(self, **kwargs):
        num_threads = kwargs["n_threads"]
        address = kwargs["address"]
        port = kwargs["port"]
        threads = []

        self.simple_http_client_get = SimpleHttpLogClientGet(address, port)
        self.simple_http_client_post = SimpleHttpLogClientPost(address, port)

        for i in range(num_threads):
            threads.append(
                threading.Thread(
                    target=self._kubernetes_job, name=i, kwargs=kwargs
                )
            )

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

            if randrange(1, 100) < read_rate:
                self._write_work(**kwargs)
            else:
                self._read_work(**kwargs)

            index += 1
            time.sleep(thinking_time)

    def _write_work(self, **kwargs):
        payload_size = kwargs["payload_size"]

        gibberish_http_json = GibberishHttpJson(payload_size, as_json=True)
        gibberish_content = gibberish_http_json.perform()

        if threading.current_thread().name == '1':
            self._calculate_latency_time_between_post_request(
                self.simple_http_client_post, gibberish_content
            )
            return

        self.simple_http_client_post.perform(gibberish_content)

    def _calculate_latency_time_between_post_request(self, client: SimpleHttpLogClientPost, gibberish_content: list):
        st = int(time.time_ns() / 1e3)
        client.perform(gibberish_content)
        et = int(time.time_ns() / 1e3)
        printf_mutex.acquire()
        print(f"{et} {et - st}")
        printf_mutex.release()

    def _read_work(self, **kwargs):
        qty_iteration = kwargs["qty_iteration"]
        line_number = randrange(qty_iteration)

        if threading.current_thread().name == '1':
            self._calculate_latency_time_between_get_request(
                self.simple_http_client_get, line_number
            )
            return

        self.simple_http_client_get.perform(line_number=line_number)

    def _calculate_latency_time_between_get_request(self, client: SimpleHttpLogClientGet, line_number: int):
        st = int(time.time_ns() / 1e3)
        client.perform(line_number=line_number)
        et = int(time.time_ns() / 1e3)
        printf_mutex.acquire()
        print(f"{et} {et - st}")
        printf_mutex.release()


@click.command()
@click.option("--address",             default="localhost", help="Set server address")
@click.option("--port",                default=8000,        help="Set server port")
@click.option("--payload_size",        default=1,           help="Set the payload size")
@click.option("--qty_iteration",       default=1e5,         help="Set the key range to determine the volume")
@click.option("--read_rate",           default=50,          help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads",           default=2,           help="Set number of client threads")
@click.option("--thinking_time",       default=0.2,         help="Set thinking time between requests")
@click.option("--duration",            default=1.5,         help="Set duration in seconds")
def hello(**kwargs):
    StressGenerator().perform(**kwargs)


if __name__ == '__main__':
    hello()
