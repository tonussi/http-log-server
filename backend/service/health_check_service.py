from service.secondary_backup_health_check import SecondaryBackupHealthCheck

class HealthCheckService(object):
    """
    Receiver Controller 
    """

    def perform(self):
        """
        only public method that will perform the desired operation
        and maybe return some response for coordination of the rest
        """
        return self._all_managers()

    # private

    def _all_managers(self) -> dict:
        """
        check managers statuses return a dict to the endpoint
        """
        return {
            "healthy_check": {
                replica_manager_id: SecondaryBackupHealthCheck(secondary_backup_id=replica_manager_id).perform() for replica_manager_id in range(3)
            }
        }
