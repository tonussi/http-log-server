import os


class DirGetter(object):
    def source_latency_log(self) -> str:
        return os.environ.get("LATENCY_LOG")
