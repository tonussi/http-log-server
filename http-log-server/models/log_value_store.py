
from service.data_source_writer_service import DataSourceWriterService
from service.text_line_service import TextLineService


class  LogValueStore(object):
    def __init__(self) -> None:
        self.db_writer = DataSourceWriterService()
        self.db_reader = TextLineService()

    def populate(self):
        for index in range(1000):
            self.add(f"automatic-populated-{index}")

    def add(self, payload):
        self.db_writer.perform(payload)

    def get(self, line_number):
        return self.db_reader.perform(line_number)
