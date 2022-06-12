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

        self.do_get_request = SimpleHttpLogClientGet(address, port)
        self.do_post_request = SimpleHttpLogClientPost(address, port)

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
        random_content = gibberish_http_json.perform()

        if threading.current_thread().name == '1':
            printf_mutex.acquire()
            self._calculate_latency_time_between_request(self.do_post_request, random_content)
            printf_mutex.release()
            return

        try:
            self.do_post_request.perform(random_content)
        except:
            pass

    def _read_work(self, **kwargs):
        qty_iteration = kwargs["qty_iteration"]
        line_number = randrange(qty_iteration)

        if threading.current_thread().name == '1':
            printf_mutex.acquire()
            self._calculate_latency_time_between_request(self.do_get_request, line_number)
            printf_mutex.release()
            return

        try:
            self.do_get_request.perform(line_number=line_number)
        except:
            pass

    ###########
    # Latency #
    ###########

    def _calculate_latency_time_between_request(self, client, content):
        st = time.time_ns()
        client.perform(content)
        et = time.time_ns()
        print(f"{time.time_ns()} {self._delta_microseconds(et, st)}")

    def _delta_microseconds(self, et, st):
        return int((et / 1e3) - (st / 1e3))

    def _delta_nanoseconds(self, et, st):
        return et - st


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
