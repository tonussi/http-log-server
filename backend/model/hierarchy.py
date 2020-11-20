from enum import Enum


class Hierarchy(Enum):
    """
    Replica Manager Hierarchy
    """
    PRIMARY_BACKUP = 0
    SECONDARY_BACKUP = 1
