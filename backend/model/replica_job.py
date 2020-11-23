from multiprocessing import Process
from model.replica_manager import ReplicaManager
from model.errors.missing_requirement import MissingRequirement


class ReplicaJob(object):
    """
    Job description to be enqueued in a queue of works
    """
    def __init__(self, replica_manager: ReplicaManager, job_id: int, image_id: int, description: dict):
        self.job_id = job_id
        self.image_id = image_id

        self.Overseer().perform(description)

        self.description = {"action": "replication", "resource": None}

        self.replica_manager = replica_manager

        self.process_instance = None

    def do_task(self):
        self.process_instance = Process(target=self.perform, args=('bob',))
        self.process_instance.start()
        self.process_instance.join()

    def perform(self):
        self.replica_manager.perform()

    class Overseer(object):
        """
        Validation of parameters and alike for the class Job
        """
        def perform(self, description: dict) -> bool:
            if not description["action"]:
                raise MissingRequirement("{} is missing".format(description))
            if not description["resource"]:
                raise MissingRequirement("{} is missing".format(description))
            return True
