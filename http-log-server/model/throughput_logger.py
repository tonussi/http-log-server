import os
import csv
from time import time_ns

from model.helpers import DirGetter

class ThroughputLogger(object):
    """
    Fake simulator of db csv writting service
    Replica Writer Service is a more complex class
    because if the client writes in a replica then Primary Backup
    must be called after this operation in order to let every
    backup equal
    """

    def __init__(self):
        self.dir_getter = DirGetter()
        self.csv_file = self.dir_getter.source_thoughput_log()
        self.file_directory = os.path.split(self.csv_file)[0]
        self.file_name = os.path.split(self.csv_file)[1]

        if not os.path.isdir(self.file_directory): os.makedirs(self.file_directory)
        if not os.path.isfile(self.csv_file):
            with open(self.csv_file, 'a+', newline='') as csvfile: csvfile.close()
            self._append_data()

    def perform(self):
        self._write()

    # private

    def _write(self):
        self._append_data()

    def _current_counter(self):
        csvfile = open(self.csv_file, 'r')
        reader = csv.reader(csvfile, delimiter=';')
        all_lines = list(reader)

        if len(all_lines) > 0:
            last_line = all_lines[-1]
        else:
            last_line = [time_ns(), 0]
        return last_line

    def _append_data(self):
        try:
            last_line = self._current_counter()
            current_time = time_ns() - int(last_line[0])
            counter = int(last_line[1]) + 1

            with open(self.csv_file, 'a+', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(
                    [
                        current_time,
                        counter
                    ]
                )
                csvfile.close()
        except IOError:
            return False

        return True
