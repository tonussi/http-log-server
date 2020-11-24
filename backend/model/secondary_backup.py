import os
from shutil import copyfile
from model.image import Image
from model.secondary_status import SecondaryStatus


class SecondaryBackup(object):
    """
    The replica manager is a subsystem that is responsible for managing the synchronization of replicas.
    Source: https://docs.aws.amazon.com/lumberyard/latest/userguide/network-replicas-replica-manager.html
    """

    def __init__(self, replica_manager_id: int, image: Image):
        self.image = image
        self.replica_manager_id = replica_manager_id

    def __del__(self):
        del self.image

    def _is_fine(self) -> int:
        return SecondaryStatus.HEALTHY
