import os
from shutil import copyfile
from model.image import Image
from model.hierarchy import Hierarchy
from model.replica_manager import ReplicaManager
from model.secondary_status import SecondaryStatus


class SecondaryBackup(ReplicaManager):
    """
    The replica manager is a subsystem that is responsible for managing the synchronization of replicas.
    Source: https://docs.aws.amazon.com/lumberyard/latest/userguide/network-replicas-replica-manager.html
    """
    def __init__(self, replica_manager_id: int, image: Image, hierarchy: Hierarchy):
        self.image = image
        self.replica_manager_id = replica_manager_id
        self.hierarchy = hierarchy or Hierarchy.SECONDARY_BACKUP
