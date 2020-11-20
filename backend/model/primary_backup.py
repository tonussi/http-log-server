from model.image import Image
from model.job_queue import JobQueue
from model.hierarchy import Hierarchy
from model.replica_job import ReplicaJob
from model.secondary_status import SecondaryStatus


class PrimaryBackup(object):
    """
    docstring
    """

    def __init__(self, replica_manager_id: int, image: Image, secondaries: dict, hierarchy: Hierarchy):
        """
        docstring
        """
        self.last_id = 0
        self.image = image
        self.job_queue = JobQueue()
        self.secondaries = secondaries
        self.replica_manager_id = replica_manager_id
        self.hierarchy = hierarchy or Hierarchy.PRIMARY_BACKUP

    def perform(self):
        """
        docstring
        """
        for secondary in self.secondaries:
            self.job_queue.put(self._new_job(secondary))

    # private

    def _next_job_id(self) -> int:
        return self.last_id + 1

    def _new_job(self, secondary: Image) -> ReplicaJob:
        return ReplicaJob(job_id=self._next_job_id(), image_id=secondary.id, description={})

    def _check_all_secondary_health(self) -> dict:
        """
        docstring
        """
        if all(self.secondaries[secondary_id].is_fine() == SecondaryStatus.HEALTHY for secondary_id in self.secondaries):
            return {"status": True}

        problematic_replica_managers = {}
        for secondary in self.secondaries:
            if secondary.status != SecondaryStatus.HEALTHY:
                problematic_replica_managers[secondary.replica_manager_id] = secondary
        return problematic_replica_managers
