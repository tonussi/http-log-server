import os
import time
from models.helpers import DirGetter
from models.image import Image
from shutil import copyfile


class ReplicaTask(object):
    """
    This is the action replication in form of a task
    """

    def __init__(self, image: Image, secondary_backup_id: int):
        self.image = image
        self.dir_getter = DirGetter()
        self.secondary_backup_id = secondary_backup_id

    def __call__(self):
        self._copy()
        self._add_md5_file()
        return str(self.image)

    def __str__(self):
        return str(self.image)

    # private

    def _copy(self) -> bool:
        copyfile(self.image.file_absolute_path,
                 f"{self.dir_getter.backups_dir()}/{self.secondary_backup_id}/operations.log")

    def _add_md5_file(self) -> bool:
        file_check_sum = self.image.perform()

        with open(f"{self.dir_getter.backups_dir()}/{self.secondary_backup_id}/checksum.txt", "w") as image_file:
            image_file.write(file_check_sum)
            image_file.close()
