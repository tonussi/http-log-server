import multiprocessing

from model.image import Image
from model.replica_job import ReplicaJob
from model.replica_task import ReplicaTask
from model.secondary_backup import SecondaryBackup
from model.secondary_status import SecondaryStatus


class PrimaryBackup(object):
    """
    Main administrator of the secondary backups
    Primary Backup created a n+1 secondary backups
    +1 because its his primary backup as well
    I tried to make everything more of the same thing
    to make things easier to implement
    """
    def __init__(self, image: Image, secondaries: list):
        self.image = image
        self.primary_backup_id = 0

        self._prepare_secondaries(secondaries)

        self.secondaries = [SecondaryBackup(self.primary_backup_id, self.image)] + self.secondaries

        self.last_id = 0
        self.replica_tasks = None
        self.replica_results = None
        self.num_consumers = len(self.secondaries)

    def perform(self):
        # I used the following tutorial https://pymotw.com/2/multiprocessing/communication.html, to code this method perform

        # Establish communication queues
        self.replica_tasks = multiprocessing.JoinableQueue()
        self.replica_results = multiprocessing.Queue()

        # Start consumers
        print('Creating %d consumers' % self.num_consumers)
        consumers = []
        for secondary in range(self.secondaries):
            consumers.append(self._new_job(secondary))
        for w in consumers:
            w.start()

        # Enqueue jobs
        num_jobs = 10
        for secondary in range(self.num_consumers):
            self.replica_tasks.put(ReplicaTask(secondary.image))

        # Add a poison pill for each consumer
        for _ in range(self.num_consumers):
            self.replica_tasks.put(None)

        # Wait for all of the replica_tasks to finish
        self.replica_tasks.join()

        # Start printing replica_results
        while num_jobs:
            result = self.replica_results.get()
            print('Result:', result)
            num_jobs -= 1

    # private

    def _prepare_secondaries(self, secondaries: list) -> list:
        if len(secondaries) > 0:
            # means the outside had have set
            self.secondaries = secondaries
        else:
            self.secondaries = [SecondaryBackup(self.primary_backup_id, self.image)]

    def _next_job_id(self) -> int:
        return self.last_id + 1

    def _new_job(self, secondary: SecondaryBackup) -> ReplicaJob:
        return ReplicaJob(self.replica_tasks, self.replica_results, secondary, self._next_job_id(), {})

    def _check_all_secondary_health(self) -> dict:
        if all(self.secondaries[secondary_id]._is_fine() == SecondaryStatus.HEALTHY for secondary_id in self.secondaries):
            return {"status": True}

        problematic_replica_managers = {}
        for secondary in self.secondaries:
            if secondary._is_fine != SecondaryStatus.HEALTHY:
                problematic_replica_managers[secondary.replica_manager_id] = secondary
        return problematic_replica_managers
