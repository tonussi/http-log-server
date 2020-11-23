from model.image import Image
from model.job_queue import JobQueue
from model.hierarchy import Hierarchy
from model.replica_job import ReplicaJob
from model.replica_manager import ReplicaManager
from model.secondary_status import SecondaryStatus


class PrimaryBackup(ReplicaManager):
    """
    Main administrator of the secondary backups
    """
    def __init__(self, replica_manager_id: int, image: Image, secondaries: dict, hierarchy: Hierarchy):
        self.last_id = 0
        self.image = image
        self.job_queue = JobQueue()
        self.secondaries = secondaries
        self.replica_manager_id = replica_manager_id
        self.hierarchy = hierarchy or Hierarchy.PRIMARY_BACKUP

    def perform(self):
        for secondary in self.secondaries:
            self.job_queue.put(self._new_job(secondary))

        self.job_queue.join()

    # private

    def _next_job_id(self) -> int:
        return self.last_id + 1

    def _new_job(self, secondary: Image) -> ReplicaJob:
        return ReplicaJob(job_id=self._next_job_id(), image_id=secondary.id, description={})

    def _check_all_secondary_health(self) -> dict:
        if all(self.secondaries[secondary_id]._is_fine() == SecondaryStatus.HEALTHY for secondary_id in self.secondaries):
            return {"status": True}

        problematic_replica_managers = {}
        for secondary in self.secondaries:
            if secondary.status != SecondaryStatus.HEALTHY:
                problematic_replica_managers[secondary.replica_manager_id] = secondary
        return problematic_replica_managers
