import os
import time
from shutil import copyfile

class ReplicaTask(object):
    def __init__(self, image):
        self.image = image

    def __call__(self):
        time.sleep(0.1)

        self._copy()
        self._add_md5_file()

        return '%s' % (self.image)

    def __str__(self):
        return '%s * %s' % (self.image)

    def perform(self):
        self._copy()
        self._add_md5_file()

    # private

    def _copy(self) -> bool:
        copyfile(self.image.file_absolute_path, self.image.destination_folder)

    def _add_md5_file(self) -> bool:
        file_check_sum = self.image.md5()

        with open(f"{self.image.image_directory}/checksum.txt", "w") as image_file:
            image_file.write(file_check_sum)
            image_file.close()
