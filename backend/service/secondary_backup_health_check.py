import os

class SecondaryBackupHealthCheck(object):
    """
    Secondary Backup Health Check Getter
    """
    def __init__(self, secondary_backup_id: int):
        self.secondary_backup_id = secondary_backup_id
        self.backup_dir = os.environ.get("BACKUPS_DIR")

    def perform(self) -> str:
        checksum_path_content = self._get_checksum_content()
        return checksum_path_content

    def _get_checksum_content(self):
        checksum_path_path = f"{self.backup_dir}/{self.secondary_backup_id}/checksum.txt"
        checksum_path_content = None
        try:
            with open(checksum_path_path, 'r') as checksum_file:
                checksum_path_content = checksum_file.read()
                checksum_file.close()
        except IOError:
            return "checksum is not present"
        return checksum_path_content
