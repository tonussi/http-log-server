import time
import multiprocessing
from model.errors.missing_requirement import MissingRequirement


class ReplicaJob(multiprocessing.Process):
    """
    Job description to be enqueued in a queue of works
    """
    def __init__(self, task_queue, result_queue, job_id: int, description: dict):
        multiprocessing.Process.__init__(self)
        self.job_id = job_id

        self.Overseer().perform(description)

        self.description = {"action": "replication", "resource": None}
        self.replica_manager = replica_manager
        self.process_instance = None
        self.task_queue = task_queue
        self.result_queue = result_queue

    class Overseer(object):
        """
        Validation of parameters and alike for the class Job
        """
        def perform(self, description: dict) -> bool:
            missing_str = "{} is missing"

            if not description["action"]:
                raise MissingRequirement(missing_str.format(description))
            if not description["resource"]:
                raise MissingRequirement(missing_str.format(description))
            return True

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print('%s: Exiting' % proc_name)
                self.task_queue.task_done()
                break
            print('%s: %s' % (proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
