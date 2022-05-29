class MissingRequirement(Exception):
    """
    Exception for missing requirements
    """
    pass

class ReplicaNodeDoesNotExist(Exception):
    """
    When client tries to change a non existent replica
    """
    pass
