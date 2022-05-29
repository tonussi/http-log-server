import os
import csv
import time
from models.helpers import DirGetter
import multiprocessing


class Statistics(object):
    """
    Fake simulator of db csv writting service
    Replica Writer Service is a more complex class
    because if the client writes in a replica then Primary Backup
    must be called after this operation in order to let every
    backup equal
    """

    def __init__(self):
        self.dir_getter = DirGetter()
        self.stats_file = self.dir_getter.source_thoughput_log()
        self.file_directory = os.path.split(self.stats_file)[0]
        self.file_name = os.path.split(self.stats_file)[1]

        if not os.path.isdir(self.file_directory):
            os.makedirs(self.file_directory)
        if not os.path.isfile(self.stats_file):
            with open(self.stats_file, 'a+', newline='') as f:
                f.close()
            self._append_data()

    def perform(self):
        self._increment_counter()

    # private

    def _worker(self):
        time.sleep(1)
        self._write()
        # print(time.time_ns())

    def _increment_counter(self):
        multiprocessing.Process(target=self._worker).start()

    def _write(self):
        self._append_data()

    def _current_counter(self):
        f = open(self.stats_file, 'r')
        reader = csv.reader(f, delimiter='\t')
        all_lines = list(reader)

        if len(all_lines) > 0:
            last_line = all_lines[-1]
        else:
            last_line = [time.time_ns(), 0]
        return last_line

    def _append_data(self):
        try:
            last_line = self._current_counter()
            current_time = time.time_ns()
            counter = str(int(last_line[1]) + 1)

            with open(self.stats_file, 'a+') as f:
                spamwriter = csv.writer(f, delimiter='\t')
                spamwriter.writerow([current_time, counter])
                f.close()
        except IOError:
            return False

        return True
