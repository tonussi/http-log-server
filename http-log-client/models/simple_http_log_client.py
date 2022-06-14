import requests
import requests.exceptions


class SimpleHttpLogClientPost(object):
    def __init__(self, address, port) -> None:
        self.api_url = f"http://{address}:{port}"
        self.session = requests.Session()

    def perform(self, body_json_content):
        return self._simple_requests_scenario(body_json_content)

    # private

    def _simple_requests_scenario(self, body_json_content):
        return self.session.post(f"{self.api_url}/insert", body_json_content)


class SimpleHttpLogClientGet(object):
    def __init__(self, address, port) -> None:
        self.api_url = f"http://{address}:{port}"
        self.session = requests.Session()

    def perform(self, line_number):
        return self._simple_requests_scenario(line_number)

    # private

    def _simple_requests_scenario(self, line_number):
        return self.session.get(f"{self.api_url}/line/{line_number}")
