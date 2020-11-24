import os
import time
from model.image import Image
from shutil import copyfile

class ReplicaTask(object):
    def __init__(self, image: Image, secondary_backup_id: int):
        self.image = image
        self.secondary_backup_id = secondary_backup_id

    def __call__(self):
        time.sleep(0.1)

        self._copy()
        self._add_md5_file()

        return '%s' % (self.image)

    def __str__(self):
        return str(self.image)

    def perform(self):
        self._copy()
        self._add_md5_file()

    # private

    def _copy(self) -> bool:
        copyfile(self.image.file_absolute_path, f"{self.image.file_directory}/backups/{self.secondary_backup_id}/db.csv")

    def _add_md5_file(self) -> bool:
        file_check_sum = self.image.md5()

        with open(f"{self.image.file_directory}/backups/{self.secondary_backup_id}/checksum.txt", "w") as image_file:
            image_file.write(file_check_sum)
            image_file.close()
