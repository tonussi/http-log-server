
class SecondaryBackupHealthCheck(object):
    """
    Secondary Backup Health Check Getter
    """
    def __init__(self, secondary_backup_id: int):
        self.secondary_backup_id = secondary_backup_id

    def perform(self) -> bool:
        # como que eu sei que os dados dos usuários estão salvos? eis a questão...
        # arquivos dos usuários mudaram de estados e eu preciso fazer backup
        # como saber se os backups estão saudáveis?
        return True
