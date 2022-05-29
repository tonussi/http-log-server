import time
import multiprocessing
from models.secondary_backup import SecondaryBackup


class ReplicaJob(multiprocessing.Process):
    """
    Job description to be enqueued in a queue of works
    """
    def __init__(self, task_queue, result_queue, replica_manager: SecondaryBackup):
        multiprocessing.Process.__init__(self)
        self.replica_manager = replica_manager
        self.task_queue = task_queue
        self.result_queue = result_queue

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
