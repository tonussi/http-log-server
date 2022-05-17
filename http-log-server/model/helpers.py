import os


class DirGetter(object):
    def backups_dir(self) -> str:
        return os.environ.get("BACKUPS_DIR")

    def source_db_file_path(self) -> str:
        return os.environ.get("SOURCE_DB")

    def source_thoughput_log(self) -> str:
        return os.environ.get("THROUGHPUT_LOG")
