import os
from hashlib import md5
from model.replicable import Replicable


class Image(Replicable):
    """
    Image of a file containing method to generate md5
    """
    def __init__(self, file_name: str, file_absolute_path: str):
        self.file_name = file_name
        self.file_absolute_path = file_absolute_path

        self.image_directory = os.path.split(self.file_absolute_path)[0]
        self.file_name = os.path.split(self.file_absolute_path)[1]

    def md5(self):
        hash_md5 = md5()
        with open(self.file_absolute_path, "rb") as actual_file:
            for chunk in iter(lambda: actual_file.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
