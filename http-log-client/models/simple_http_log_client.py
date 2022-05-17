import requests
import requests.exceptions


class SimpleHttpLogClientPost(object):
    def __init__(self, address, port, duration, payload_size, key_range, read_rate, n_threads, thinking_time, log_frequency, buffer_size, mutex_onoff) -> None:
        self.api_url = f"http://{address}:{port}"
        self.duration = duration
        self.payload_size = payload_size
        self.key_range = key_range
        self.read_rate = read_rate
        self.n_threads = n_threads
        self.thinking_time = thinking_time
        self.log_frequency = log_frequency
        self.buffer_size = buffer_size
        self.mutex_onoff = mutex_onoff
        self.session = requests.Session()

    def perform(self, body_json_content):
        return self._simple_requests_scenario(body_json_content)

    # private

    def _simple_requests_scenario(self, body_json_content):
        return self.session.post(f"{self.api_url}/db", json=body_json_content).content


class SimpleHttpLogClientGet(object):
    def __init__(self, address, port, duration, payload_size, key_range, read_rate, n_threads, thinking_time, log_frequency, buffer_size, mutex_onoff) -> None:
        self.api_url = f"http://{address}:{port}"
        self.duration = duration
        self.payload_size = payload_size
        self.key_range = key_range
        self.read_rate = read_rate
        self.n_threads = n_threads
        self.thinking_time = thinking_time
        self.log_frequency = log_frequency
        self.buffer_size = buffer_size
        self.mutex_onoff = mutex_onoff
        self.session = requests.Session()

    def perform(self, line_number):
        return self._simple_requests_scenario(line_number)

    # private

    def _simple_requests_scenario(self, line_number):
        return self.session.get(f"{self.api_url}/line?number={line_number}").content
