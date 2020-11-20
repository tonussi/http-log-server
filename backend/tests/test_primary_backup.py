import unittest
from model.image import Image
from model.hierarchy import Hierarchy
from model.replica_manager import ReplicaManager
from model.primary_backup import PrimaryBackup

class TestPrimaryBackup(unittest.TestCase):
    def setUp(self):
        image = Image("test_file.txt", "./tests/test_file.txt")

        replica_manager = ReplicaManager(replica_manager_id=1, image=image, hierarchy=Hierarchy.SECONDARY_BACKUP)

        secondaries = {}
        secondaries[replica_manager.replica_manager_id] = replica_manager

        primary_backup = PrimaryBackup(replica_manager_id=0, image=image, secondaries=secondaries, hierarchy=Hierarchy.PRIMARY_BACKUP)

        self.action = primary_backup._check_all_secondary_health()

    def test_secondary_checks_out(self):
        self.assertEqual(self.action, {'status': True})


if __name__ == '__main__':
    unittest.main()
