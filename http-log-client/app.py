import psutil
import secrets
import time
from multiprocessing import Process
from random import randrange
from string import ascii_uppercase

import click

from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)


class StressGenerator(Process):
    def __init__(self, **kwargs) -> None:
        self.arguments = kwargs

        port = self.arguments["port"]
        address = self.arguments["address"]

        self.do_get_request = SimpleHttpLogClientGet(address, port)
        self.do_post_request = SimpleHttpLogClientPost(address, port)

        Process.__init__(self)

        self._set_priority()

    def run(self):
        duration = self.arguments["duration"]
        read_rate = self.arguments["read_rate"]
        thinking_time = self.arguments["thinking_time"]

        timeout = time.time() + 60 * duration
        iteration_index = 1

        while True:
            if time.time() > timeout:
                break

            if randrange(1, 100) < read_rate:
                self._read_work(iteration_index)
            else:
                self._write_work()

            iteration_index += 1
            time.sleep(thinking_time)

        exit(0)

    def _write_work(self):
        bytes_size = self.arguments["bytes_size"]
        random_bytes_string_format = self._random_string(bytes_size)
        encode_bytes_as_base64 = random_bytes_string_format.encode("utf-8")
        self.do_post_request.perform(encode_bytes_as_base64)

    def _read_work(self, iteration_index):
        line_number = randrange(iteration_index << 9)
        self.do_get_request.perform(line_number=line_number)

    def _random_string(self, bytes_size):
        random_bytes_string_format = ""
        for _ in range(bytes_size):
            random_bytes_string_format += secrets.choice(ascii_uppercase)
        return random_bytes_string_format

    def _set_priority(self):
        self.daemon = True

class StressGeneratorLogger(StressGenerator):
    def _write_work(self):
        bytes_size = self.arguments["bytes_size"]
        random_bytes_string_format = self._random_string(bytes_size)
        encode_bytes_as_base64 = random_bytes_string_format.encode("utf-8")
        self._calculate_latency(self.do_post_request, encode_bytes_as_base64)

    def _read_work(self, iteration_index):
        self._calculate_latency(self.do_get_request, iteration_index << 9)

    def _calculate_latency(self, client, content):
        st = time.time_ns()
        client.perform(content)
        et = time.time_ns()
        print(f"{et} {et - st}")

    def _set_priority(self):
        parent = psutil.Process()
        parent.nice(0)



@click.command()
@click.option("--address",             default="localhost", help="Set server address")
@click.option("--port",                default=8000,        help="Set server port")
@click.option("--bytes_size",          default=128,         help="Set the payload size in number of bytes")
@click.option("--read_rate",           default=50,          help="Set the reading rate from 0 to 100 percent")
@click.option("--n_processes",         default=1,           help="Set number of client processes")
@click.option("--thinking_time",       default=0.2,         help="Set thinking time between requests")
@click.option("--duration",            default=1.5,         help="Set duration in seconds")
def hello(**kwargs):
    processes = []

    processes_count = kwargs["n_processes"]

    sgl = StressGeneratorLogger(**kwargs)
    processes.append(sgl)

    for _ in range(processes_count - 1):
        processes.append(StressGenerator(**kwargs))

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    hello()
