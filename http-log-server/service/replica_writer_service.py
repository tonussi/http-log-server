import os
import csv
from shutil import copyfile
from models.helpers import DirGetter
from models.primary_backup import PrimaryBackup
from models.errors.primary_backup_exceptions import ReplicaNodeDoesNotExist

class ReplicaWriterService(object):
    """
    Fake simulator of db csv writting service
    Replica Writer Service is a more complex class
    because if the client writes in a replica then Primary Backup
    must be called after this operation in order to let every
    backup equal
    """

    def __init__(self, which_replica: int):
        self.dir_getter = DirGetter()

        self._prepare_which_replica(which_replica)

        self.csv_columns = ["operation", "name", "city"]
        self.csv_file = f"{self.dir_getter.backups_dir()}/{which_replica}/operations.log"

        self.file_directory = os.path.split(self.csv_file)[0]
        self.file_name = os.path.split(self.csv_file)[1]

        if not os.path.isdir(self.file_directory):
            os.makedirs(self.file_directory)

    def perform(self, params):
        if not self.which_replica: return f"this replica node inst set to be used"
        if len(params) == 0: return "nothing to insert"

        if not self._write(params): return f"io problem with the writing stage of the replica number {self.which_replica}"
        if not self._move_to_source(): return f"io problem with the copying stage of the replica number {self.which_replica}"
        if self._invoke_primary_backup_management(): return f"successfully changed data at node={self.which_replica} and your data was replicated to other nodes"
        return f"processes failed to replicate data {self.which_replica}"

    # private

    def _invoke_primary_backup_management(self):
        try:
            PrimaryBackup().perform()
        except IOError:
            return False
        return True

    def _move_to_source(self):
        try:
            copyfile(self.csv_file, self.dir_getter.source_db_file_path())
        except IOError:
            return False
        return True

    def _prepare_which_replica(self, which_replica):
        self.which_replica = None if which_replica < 0 or which_replica > 2 else which_replica

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
