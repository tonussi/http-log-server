from model.errors.missing_requirement import MissingRequirement


class ReplicaJob(object):
    """
    Job description to be enqueued in a queue of works
    """
    def __init__(self, job_id: int, image_id: int, description: dict):
        self.job_id = job_id
        self.image_id = image_id

        self.Overseer().perform(description)

        self.description = {"action": "replication", "resource": None}

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
