from service.secondary_backup_health_check import SecondaryBackupHealthCheck

class HealthCheckService(object):
    """
    Receiver Controller 
    """

    # public

    def perform(self):
        """
        only public method that will perform the desired operation
        and maybe return some response for coordination of the rest
        """
        return self._managers_statuses()

    # private

    def _managers_statuses(self) -> dict:
        """
        check managers statuses return a dict to the endpoint
        """
        return {
            "SecondaryBackupHealthCheck 0": SecondaryBackupHealthCheck(secondary_backup_id=0).perform(),
            "SecondaryBackupHealthCheck 1": SecondaryBackupHealthCheck(secondary_backup_id=1).perform(),
            "SecondaryBackupHealthCheck 2": SecondaryBackupHealthCheck(secondary_backup_id=2).perform(),
        }
