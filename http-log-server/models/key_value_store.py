import json, os
from models.helpers import DirGetter

class KeyValueStore(object):
    def __init__(self, key_space) -> None:
        self.kv = {}
        self.index = 0
        self.key_space = key_space or 1e9
        self.dir_getter = DirGetter()
        self.kv_columns = ["operation", "name", "city"]
        self.kv_file = self.dir_getter.source_db_file_path()
        self.file_directory = os.path.split(self.kv_file)[0]
        self.file_name = os.path.split(self.kv_file)[1]

        if not os.path.isdir(self.file_directory):
            os.makedirs(self.file_directory)

    def get(self, key):
        return self.kv.get(key, None)

    def add(self, value):
        self.kv[self.index % self.key_space] = value
        self.index += 1

    def persist(self):
        with open(self.kv_file, 'w') as fp:
            json.dump(self.file , fp)
