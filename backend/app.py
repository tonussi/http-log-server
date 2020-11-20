from control import ReceiverController

class Run(object):
    """
    Backend Api Runner
    """

    def replicate(self, file_id):
        ReceiverController.perform(file_id)
