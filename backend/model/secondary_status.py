from enum import Enum


class SecondaryStatus(object):
    """
    Status of the Secondary Replica Manager
    """

    HEALTHY = 0
    COMPLETE = 1
    PROCESSING = 2
    CORRUPTED_FILE = 3
