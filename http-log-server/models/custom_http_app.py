import re
import json
import socketserver
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler
from multiprocessing import Process, Value

from service.data_source_writer_service import DataSourceWriterService
from service.text_line_service import TextLineService

CONTADOR_GLOBAL = Value('d', 0.0)


class CustomHttpHandler(BaseHTTPRequestHandler):
    # def __init__(self, request, client_address, server) -> None:
    #     super().__init__(request, client_address, server)

    # def log_message(self, format, *args):
    #     return

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        split_result = urllib.parse.urlsplit(self.path)
        print(f"do_GET from {self.client_address} received this path {self.path}")

        # import pdb; pdb.set_trace()
        parsed_path = re.findall("(/line/)(-?\d+)", self.path)

        information = {}
        if split_result.path == '/':
            information = self._base_url()
        if len(parsed_path):
            information = self._text_line(int(parsed_path[0][1]))

        # print(information)
        self.wfile.write(bytes(json.dumps(information), 'utf-8'))

        CONTADOR_GLOBAL.value += 1

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        # import pdb; pdb.set_trace()
        print(f"do_POST from {self.client_address} received this body {post_body} at this path {self.path}")

        if self.path == '/db':
            self._send_data_to_file(post_body)

        self.wfile.write(post_body)

        CONTADOR_GLOBAL.value += 1

    # private
    # get

    def _text_line(self, number):
        # prepared_query_params = int(urllib.parse.parse_qs(query_params)['number'][0])
        return TextLineService().perform(number)

    def _base_url(self):
        return {"status": 200}

    # post

    def _send_data_to_file(self, http_json):
        if http_json == b'': return json.dumps({"status": 401})
        if http_json == None: return json.dumps({"status": 401})
        if type(http_json)==list and len(http_json) <= 0: return json.dumps({"status": 401})
        if type(http_json)==dict and len(http_json) <= 0: return json.dumps({"status": 401})
        prepared_http_json = json.loads(http_json)
        DataSourceWriterService().perform(prepared_http_json['batch'])


class CustomHttpApp(object):
    def __init__(self, **kwargs) -> None:
        self.tcp_ip = kwargs["address"]
        self.tcp_port = kwargs["port"]

        self.p = Process(target=self.statistics, args=[CONTADOR_GLOBAL])
        self.p.start()

    def statistics(self, *args):
        throughput = args[0]
        previous_throughput = 0.0
        while True:
            time.sleep(1)
            thr = throughput.value - previous_throughput
            previous_throughput = throughput.value
            # print(f"{time.time_ns()} {thr}")

    def perform(self):
        try:
            with socketserver.TCPServer((self.tcp_ip, self.tcp_port), CustomHttpHandler) as httpd:
                httpd.serve_forever()
        except:
            self.p.join()
