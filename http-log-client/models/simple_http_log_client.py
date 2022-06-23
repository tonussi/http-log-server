from random import randrange
import time
import requests
import requests.exceptions


class SimpleHttpLogClientPost(object):
    def __init__(self, address, port) -> None:
        self.api_url = f"http://{address}:{port}"
        self.session = requests.Session()

    def perform(self, body_json_content):
        time.sleep(randrange(100) / 1e5)
        try:
            return self._simple_requests_scenario(body_json_content)
        except:
            pass

    # private

    def _simple_requests_scenario(self, body_json_content):
        return self.session.post(f"{self.api_url}/insert", body_json_content)


class SimpleHttpLogClientGet(object):
    def __init__(self, address, port) -> None:
        self.api_url = f"http://{address}:{port}"
        self.session = requests.Session()

    def perform(self, line_number):
        time.sleep(randrange(100) / 1e5)
        try:
            return self._simple_requests_scenario(line_number)
        except:
            pass

    # private

    def _simple_requests_scenario(self, line_number):
        return self.session.get(f"{self.api_url}/line/{line_number}")
