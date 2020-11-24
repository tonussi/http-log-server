import os
import csv
from model.helpers import DirGetter

class DbWriterService(object):
    """
    Fake simulator of db csv writting service
    """

    def __init__(self):
        self.dir_getter = DirGetter()
        self.csv_columns = ["No", "Name", "Country"]
        self.csv_file = self.dir_getter.source_db_file_path()

        self.file_directory = os.path.split(self.csv_file)[0]
        self.file_name = os.path.split(self.csv_file)[1]

        if not os.path.isdir(self.file_directory):
            os.makedirs(self.file_directory)

    def perform(self, params):
        return self._write(params)

    # private

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
