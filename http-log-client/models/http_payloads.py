import os
from models.http_payload_types import HttpPayloadType

class HttpPayloadBodyGenerator():
    def __init__(self, body_json_content, request_type, route_path) -> None:
        self.body_json_content = body_json_content
        self.request_type = request_type
        self.route_path = route_path

    def perform(self, http_payload_type):
        if http_payload_type is HttpPayloadType.HTTP_DEFAULT:
            return self._http_request_text()
        return "Invalid HttpPayloadType argument"

    # private

    def _utf8_len(self, text_to_encode):
        return len(text_to_encode.encode('utf-8'))

    def _http_request_text(self):
        simple_http_body_document = f"""{self.request_type} {self.route_path} HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Content-Length: {self._utf8_len(self.body_json_content)}

{self.body_json_content}"""

        if os.environ.get("DEBUG", False):
            print(simple_http_body_document)

        return simple_http_body_document
