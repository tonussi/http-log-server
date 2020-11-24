import csv


class DbWriterService(object):
    """
    Fake simulator of db csv writting service
    """

    def __init__(self):
        self.csv_columns = ["No", "Name", "Country"]
        self.csv_file = "/db.csv"

    def perform(self, params):
        return self._write(params)

    # private

    def _write(self, params):
        success_check = True
        try:
            with open(self.csv_file, "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.csv_columns)
                writer.writeheader()
                for data in params:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
            success_check = False
        return success_check
