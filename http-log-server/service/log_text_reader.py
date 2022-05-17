import os
from model.image import Image
from model.helpers import DirGetter

class LogTextReader(object):
    """
    Secondary Backup Health Check Getter
    """
    def __init__(self):
        self.dir_getter = DirGetter()

    def perform(self, line_number) -> str:
        log_content = self._text_at_line(line_number)
        return log_content

    def _text_at_line(self, line_number):
        result_text_line = ""
        line_number_parsed = int(line_number)
        if line_number_parsed == 0:
            line_number_parsed = 1

        try:
            with open(self.dir_getter.source_db_file_path(), 'r') as log_main_file:
                result_text_line = self._search_line_by_line_in_file(line_number_parsed, log_main_file)
                log_main_file.close()
        except IOError:
            return "log is not present"

        return result_text_line

    def _search_line_by_line_in_file(self, line_number_parsed, log_main_file):
        counter = 1

        for line in log_main_file:
            stripped_line = line.strip()

            if line_number_parsed == counter:
                return stripped_line

            counter += 1
