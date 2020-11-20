import os
from shutil import copyfile
from model.image import Image
from model.hierarchy import Hierarchy
from model.secondary_status import SecondaryStatus

class ReplicaManager(object):
    """
    The replica manager is a subsystem that is responsible for managing the synchronization of replicas.
    Source: https://docs.aws.amazon.com/lumberyard/latest/userguide/network-replicas-replica-manager.html
    """

    def __init__(self, replica_manager_id: int, image: Image, hierarchy: Hierarchy):
        self.image = image
        self.replica_manager_id = replica_manager_id
        self.hierarchy = hierarchy or Hierarchy.SECONDARY_BACKUP

    def __del__(self):
        del self.image

    def perform(self):
        self._copy()
        self.add_md5_file()

    def _copy(self) -> bool:
        copyfile(self.image.file_absolute_path, self.image.destination_folder)

    def add_md5_file(self) -> bool:
        file_check_sum = self.image.md5()

        with open(f"{self.image.image_directory}/checksum.txt", "w") as image_file:
            image_file.write(file_check_sum)
            image_file.close()

    def is_fine(self) -> int:
      return SecondaryStatus.HEALTHY
