import os


class DataSourceWriterService(object):
    def __init__(self):
        self.log_file = "/tmp/logs/operations.log"

        self.file_directory = os.path.split(self.log_file)[0]
        self.file_name = os.path.split(self.log_file)[1]

        if not os.path.isdir(self.file_directory):
            os.makedirs(self.file_directory)

    def perform(self, row_content):
        self._append_data(row_content)

    # private

    def _append_data(self, row_content):
        with open(self.log_file, 'a+') as filewriter:
            filewriter.write(row_content)
            filewriter.write('\n')
            filewriter.close()
