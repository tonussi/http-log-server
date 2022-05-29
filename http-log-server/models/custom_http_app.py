import json
import socketserver
from http.server import BaseHTTPRequestHandler

from service.data_source_writer_service import DataSourceWriterService
from service.text_line_service import TextLineService

from models.statistics import Statistics
import urllib.parse


class CustomHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        split_result = urllib.parse.urlsplit(self.path)

        information = {}
        if split_result.path == '/':
            information = self._base_url(split_result.query)

        self.wfile.write(bytes(json.dumps(information), 'utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        information = {}

        if self.path == '/line':
            information = self._text_line(post_body)
        elif self.path == '/db':
            information = self._send_data_to_file(post_body)

        if information is None:
            self.wfile.write(post_body)
        else:
            self.wfile.write(bytes(json.dumps(information), 'utf-8'))

    # private
    # get

    def _base_url(self, parsed_params):
        return {"status": 200, "params": parsed_params}

    # post

    def _text_line(self, http_json):
        prepared_http_json = json.loads(http_json)
        information = TextLineService().perform(prepared_http_json['number'])
        Statistics().perform()
        return information

    def _send_data_to_file(self, http_json):
        prepared_http_json = json.loads(http_json)
        DataSourceWriterService().perform(prepared_http_json['batch'])
        Statistics().perform()


class CustomHttpApp(object):
    def __init__(self, **kwargs) -> None:
        self.tcp_ip = kwargs["address"]
        self.tcp_port = kwargs["port"]
        self.node_id = kwargs["node_id"]

    def perform(self):
        with socketserver.TCPServer((self.tcp_ip, self.tcp_port), CustomHttpHandler) as httpd:
            print(f"serving at {self.tcp_ip}:{self.tcp_port}")
            httpd.serve_forever()
