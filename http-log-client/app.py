import secrets
import time
from multiprocessing import Process
from random import randrange
from string import ascii_uppercase

import click
from dotenv import load_dotenv

from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)

load_dotenv()


class StressGenerator(Process):
    def __init__(self, name, **kwargs) -> None:
        self.arguments = {**kwargs, "name": name}

        port = self.arguments["port"]
        address = self.arguments["address"]

        self.do_get_request = SimpleHttpLogClientGet(address, port)
        self.do_post_request = SimpleHttpLogClientPost(address, port)

        Process.__init__(self)


    def run(self):
        duration = self.arguments["duration"]
        read_rate = self.arguments["read_rate"]
        qty_iteration = self.arguments["qty_iteration"]
        thinking_time = self.arguments["thinking_time"]

        timeout = time.time() + 60 * duration

        for _ in range(qty_iteration):
            if time.time() > timeout:
                break

            if randrange(1, 100) < read_rate:
                self._read_work()
            else:
                self._write_work()

            time.sleep(thinking_time)

        exit(0)

    def _write_work(self):
        payload_size = self.arguments["payload_size"]
        random_bytes_string_format = ''.join(secrets.choice(ascii_uppercase) for i in range(payload_size))
        encode_bytes_as_base64 = random_bytes_string_format.encode("utf-8")

        if self.arguments["name"] == 0:
            self._calculate_latency_time_between_request(
                self.do_post_request,
                encode_bytes_as_base64
            )
            return

        self.do_post_request.perform(encode_bytes_as_base64)

    def _read_work(self):
        qty_iteration = self.arguments["qty_iteration"]

        line_number = randrange(qty_iteration)

        if self.arguments["name"] == 0:
            self._calculate_latency_time_between_request(
                self.do_get_request,
                line_number
            )
            return

        self.do_get_request.perform(line_number=line_number)

    ###########
    # Latency #
    ###########

    def _calculate_latency_time_between_request(self, client, content):
        st = time.time_ns()
        client.perform(content)
        et = time.time_ns()
        print(f"{et} {self._delta_nanoseconds(et, st)}")

    def _delta_microseconds(self, et, st):
        return int((et / 1e3) - (st / 1e3))

    def _delta_nanoseconds(self, et, st):
        return et - st


@click.command()
@click.option("--address",             default="localhost", help="Set server address")
@click.option("--port",                default=8000,        help="Set server port")
@click.option("--payload_size",        default=128,         help="Set the payload size in number of bytes")
@click.option("--qty_iteration",       default=1000000,     help="Set the key range to determine the volume")
@click.option("--read_rate",           default=50,          help="Set the reading rate from 0 to 100 percent")
@click.option("--n_threads",           default=2,           help="Set number of client threads")
@click.option("--thinking_time",       default=0.2,         help="Set thinking time between requests")
@click.option("--duration",            default=1.5,         help="Set duration in seconds")
def hello(**kwargs):
    threads = []

    for i in range(kwargs["n_threads"]):
        threads.append(StressGenerator(name=i, **kwargs))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    hello()
