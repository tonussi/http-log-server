import os
import multiprocessing

from models.image import Image
from models.helpers import DirGetter
from models.replica_job import ReplicaJob
from models.replica_task import ReplicaTask
from models.secondary_backup import SecondaryBackup
from models.secondary_status import SecondaryStatus


class PrimaryBackup(object):
    """
    Main administrator of the secondary backups
    Primary Backup created a n+1 secondary backups
    +1 because its his primary backup as well
    I tried to make everything more of the same thing
    to make things easier to implement
    """

    def __init__(self):
        self.dir_getter = DirGetter()

        self._prepare_images()

        self._prepare_secondaries()

        self._prepare_dirs()

        # I used the following tutorial https://pymotw.com/2/multiprocessing/communication.html, to code this method perform
        # Establish communication queues
        self._prepare_processes()

    def perform(self):
        # Start consumers
        print('Creating %d consumers' % self.num_consumers)
        consumers = []
        for secondary in self.secondaries:
            consumers.append(self._new_job(secondary))
        for w in consumers:
            w.start()

        # Enqueue jobs
        for secondary in self.secondaries:
            self.replica_tasks.put(ReplicaTask(secondary.image, secondary.replica_manager_id))

        # Add a poison pill for each consumer
        for _ in range(self.num_consumers):
            self.replica_tasks.put(None)

        # Wait for all of the replica_tasks to finish
        self.replica_tasks.join()

        # Start printing replica_results
        num_tasks = len(self.secondaries)
        while num_tasks:
            result = self.replica_results.get()
            print('Result:', result)
            num_tasks -= 1

        return "Backups done and processes ended correctly"

    # private

    def _prepare_processes(self):
        self.replica_tasks = multiprocessing.JoinableQueue()
        self.replica_results = multiprocessing.Queue()

    def _prepare_dirs(self):
        for replica_manager_id in range(self.num_consumers):
            if not os.path.isdir(f"{self.dir_getter.backups_dir()}/{replica_manager_id}"):
                os.makedirs(f"{self.dir_getter.backups_dir()}/{replica_manager_id}")

    def _prepare_images(self):
        self.images = [Image(self.dir_getter.source_db_file_path()) for _ in range(3)]
        self.primary_backup_image = self.images[0]

    def _prepare_secondaries(self) -> list:
        self.secondaries = [SecondaryBackup(replica_manager_id, self.images[replica_manager_id]) for replica_manager_id in range(len(self.images))]
        self.num_consumers = len(self.secondaries)

    def _new_job(self, secondary: SecondaryBackup) -> ReplicaJob:
        return ReplicaJob(self.replica_tasks, self.replica_results, secondary)
