import json
import re
import socketserver
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler
from multiprocessing import Process, Value

from models.key_value_store import KeyValueStore
from models.log_value_store import LogValueStore

CONTADOR_GLOBAL = Value('i', 0)


class CustomHttpHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server) -> None:
        self.kv = KeyValueStore()
        self.log = LogValueStore()
        super().__init__(request, client_address, server)

    def log_message(self, format, *args):
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        split_result = urllib.parse.urlsplit(self.path)
        # print(f"get from {self.client_address} received this path {self.path}")

        # import pdb; pdb.set_trace()
        parsed_path = re.findall("(/line/)(-?\d+)", self.path)

        information = {}
        if split_result.path == '/':
            information = self._base_url()
        elif len(parsed_path):
            line_number = int(parsed_path[0][1])
            information = self.kv.get(line_number)
            # information = self.log.get(line_number)

        self.wfile.write(bytes(json.dumps(information), 'utf-8'))

        CONTADOR_GLOBAL.value += 1

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        # import pdb; pdb.set_trace()
        # print(f"post from {self.client_address} received this body {json.loads(post_body)} at this path {self.path}")

        if self.path == '/db':
            # self._add(post_body)
            self.kv.add(post_body)
        elif self.path == '/':
            self._base_url()

        information = {"status": 200, "message": "data has been written"}
        self.wfile.write(bytes(json.dumps(information), 'utf-8'))

        CONTADOR_GLOBAL.value += 1

    # private

    def _base_url(self):
        return {"message": "nothing to do here", "status": 200}

    # post

    def _add(self, http_json):
        if http_json == b'':
            return json.dumps({"status": 401})
        if http_json == None:
            return json.dumps({"status": 401})
        if type(http_json) == list and len(http_json) <= 0:
            return json.dumps({"status": 401})
        if type(http_json) == dict and len(http_json) <= 0:
            return json.dumps({"status": 401})
        prepared_http_json = json.loads(http_json)
        self.log.get(prepared_http_json['batch'])


class CustomHttpApp(object):
    def __init__(self, **kwargs) -> None:
        self.tcp_ip = kwargs["address"]
        self.tcp_port = kwargs["port"]
        self.throughput_delay = kwargs["throughput_delay"]

        self.p = Process(target=self.statistics, args=[CONTADOR_GLOBAL])
        self.p.start()

    def statistics(self, *args):
        throughput = args[0]
        previous_throughput = 0
        while True:
            time.sleep(self.throughput_delay)
            thr = throughput.value - previous_throughput
            previous_throughput = throughput.value
            print(f"{time.time_ns()} {thr}")

    def perform(self):
        try:
            with socketserver.TCPServer((self.tcp_ip, self.tcp_port), CustomHttpHandler) as httpd:
                httpd.serve_forever()
        except Exception as error:
            print(error)
        finally:
            self.p.join()
            exit(0)
