import socket
from models.http_payloads import HttpPayloadBodyGenerator
from models.http_payload_types import HttpPayloadType

class HttpSocketCommunicator():
    def perform(self, body_json_content, request_type="POST", route_path="/rep", address="localhost", port=5000):
        self._send(body_json_content, request_type, route_path, address, port)

    # private

    def _send(self, body_json_content, request_type, route_path, address, port):
        http_payloads = HttpPayloadBodyGenerator(body_json_content, request_type, route_path)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_connection:
            socket_connection.connect((address, port))
            socket_connection.sendall(bytes(http_payloads.perform(HttpPayloadType.HTTP_DEFAULT), 'utf-8'))
            print(str(socket_connection.recv(1024), 'utf-8'))
