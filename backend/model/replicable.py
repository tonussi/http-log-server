class Replicable(object):
    """
    Replicable interface
    """
    def perform(self):
        raise NotImplementedError

    def _md5(self):
        raise NotImplementedError
