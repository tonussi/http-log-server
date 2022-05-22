import logging
import requests
import requests.exceptions


class SimpleHttpLogClientPost(object):
    def __init__(self, address, port, node_id) -> None:
        self.api_url = f"http://{address}:{port}"
        self.session = requests.Session()
        self.node_id = node_id

    def perform(self, body_json_content):
        return self._simple_requests_scenario(body_json_content)

    # private

    def _simple_requests_scenario(self, body_json_content):
        return self.session.post(f"{self.api_url}/db", json=body_json_content).content


class SimpleHttpLogClientGet(object):
    def __init__(self, address, port, node_id) -> None:
        self.api_url = f"http://{address}:{port}"
        self.session = requests.Session()
        self.node_id = node_id

    def perform(self, line_number):
        return self._simple_requests_scenario(line_number)

    # private

    def _simple_requests_scenario(self, line_number):
        return self.session.post(f"{self.api_url}/line", json={ "number": line_number }).content
