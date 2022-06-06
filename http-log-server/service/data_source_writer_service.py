import csv
import os

from models.helpers import DirGetter


class DataSourceWriterService(object):
    def __init__(self):
        self.dir_getter = DirGetter()
        self.csv_columns = ["operation", "name", "city"]
        self.csv_file = self.dir_getter.source_db_file_path()

        self.file_directory = os.path.split(self.csv_file)[0]
        self.file_name = os.path.split(self.csv_file)[1]

        if not os.path.isdir(self.file_directory):
            os.makedirs(self.file_directory)

    def perform(self, params):
        self._worker(params)

    # private

    def _worker(self, params):
        if len(params) == 0:
            return "nothing to insert"

        if not self._write(params):
            return f"io problem with the writing stage of the replica number"
        return f"processes failed"

    def _write(self, params):
        success_check = False

        if os.path.isfile(self.csv_file):
            success_check = self._append_data(params)
        else:
            success_check = self._create_file() and self._append_data(params)

        return "rows inserted in database with success" if success_check else "rows not inserted (failed)"

    def _append_data(self, params):
        try:
            with open(self.csv_file, 'a+', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.csv_columns)
                for row_tuple in params:
                    writer.writerow(row_tuple)
                csvfile.close()
        except IOError:
            return False
        return True

    def _create_file(self):
        try:
            with open(self.csv_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.csv_columns)
                writer.writeheader()
                csvfile.close()
        except IOError:
            return False
        return True
