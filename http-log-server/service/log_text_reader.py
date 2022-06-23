import linecache

class LogTextReader(object):
    def __init__(self):
        self.log_file = "/tmp/logs/operations.log"

    def perform(self, line_number) -> str:
        return linecache.getline(self.log_file, int(line_number))
