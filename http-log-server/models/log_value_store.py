
import secrets
from string import ascii_uppercase
from service.data_source_writer_service import DataSourceWriterService
from service.text_line_service import TextLineService


class  LogValueStore(object):
    def __init__(self) -> None:
        self.db_writer = DataSourceWriterService()
        self.db_reader = TextLineService()

    def populate(self):
        for _ in range(1000):
            self.add(self._random_string(128))

    def _random_string(self, bytes_size):
        random_bytes_string_format = ""
        for _ in range(bytes_size):
            random_bytes_string_format += secrets.choice(ascii_uppercase)
        return random_bytes_string_format

    def add(self, payload):
        self.db_writer.perform(payload)

    def get(self, line_number):
        return self.db_reader.perform(line_number)
