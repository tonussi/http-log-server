import threading
import time
from random import randrange

from models.gibberish_json_generator import GibberishHttpJson
from models.simple_http_log_client import (SimpleHttpLogClientGet,
                                           SimpleHttpLogClientPost)


class StressGenerator(object):
    def perform(self, **kwargs):
        threads = []
        num_threads = kwargs["n_threads"]

        for i in range(num_threads):
            threads.append(threading.Thread(target=self._kubernetes_job, name=i, kwargs=kwargs))

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

        exit(0)


    def _write_work(self, **kwargs):
        address = kwargs["address"]
        port = kwargs["port"]
        percentage_sampling = kwargs["percentage_sampling"]
        payload_size = kwargs["payload_size"]

        gibberish_http_json = GibberishHttpJson(payload_size, as_json=True)
        gibberish_content = gibberish_http_json.perform()

        simple_http_client_post = SimpleHttpLogClientPost(address, port)

        if (randrange(100) < percentage_sampling) and (threading.current_thread().name == '1'):
            self._calculate_latency_time_between_post_request(simple_http_client_post, gibberish_content)
            return

        simple_http_client_post.perform(gibberish_content)


    def _calculate_latency_time_between_post_request(self, simple_http_client_post: SimpleHttpLogClientPost, gibberish_content: list):
        st = time.time_ns()
        simple_http_client_post.perform(gibberish_content)
        et = time.time_ns()
        print(f"{et} {str(et - st)[0:7]}")


    def _read_work(self, **kwargs):
        address = kwargs["address"]
        port = kwargs["port"]
        percentage_sampling = kwargs["percentage_sampling"]
        qty_iteration = kwargs["qty_iteration"]

        simple_http_client_get = SimpleHttpLogClientGet(address, port)

        line_number = randrange(qty_iteration)

        if (randrange(1, 100) < percentage_sampling) and (threading.current_thread().name == '1'):
            self._calculate_latency_time_between_get_request(simple_http_client_get, line_number)
            return

        simple_http_client_get.perform(line_number=line_number)


    def _calculate_latency_time_between_get_request(self, simple_http_client_get: SimpleHttpLogClientGet, line_number: int):
        st = time.time_ns()
        simple_http_client_get.perform(line_number=line_number)
        et = time.time_ns()
        print(f"{et} {str(et - st)[0:7]}")
