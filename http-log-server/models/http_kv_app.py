import json
import re
import socketserver
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler
from multiprocessing import Process, Value

from models.key_value_store import KeyValueStore

SHARED_MEM_REQUEST_COUNTER = Value('i', 0)


class CustomHttpHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server) -> None:
        self.kv = KeyValueStore()
        super().__init__(request, client_address, server)

    def log_message(self, format, *args):
        return

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        split_result = urllib.parse.urlsplit(self.path)
        # print(f"get from {self.client_address} received this path {self.path}")

        parsed_path = re.findall("(/line/)(-?\d+)", self.path)

        server_response = ""

        if split_result.path == '/':

            server_response = "nothing to do here"

        elif len(parsed_path):

            line_number = int(parsed_path[0][1])
            server_response = self.kv.get(line_number)

        self.wfile.write(bytes(json.dumps(server_response), 'utf-8'))

        SHARED_MEM_REQUEST_COUNTER.value += 1

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        # print(f"post from {self.client_address} received this body {json.loads(post_body)} at this path {self.path}")

        if self.path == '/insert':
            self.kv.add(bytes(post_body).decode('utf-8'))

        self.wfile.write(bytes("written", 'utf-8'))

        SHARED_MEM_REQUEST_COUNTER.value += 1

class HttpKvApp(object):
    def __init__(self, **kwargs) -> None:
        self.tcp_ip = kwargs["address"]
        self.tcp_port = kwargs["port"]

        self.p = Process(target=self.statistics, args=[SHARED_MEM_REQUEST_COUNTER])
        self.p.start()

    def statistics(self, *args):
        throughput = args[0]
        previous_throughput = 0
        while True:
            time.sleep(1)
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
