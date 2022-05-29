import unittest
from models.image import Image
from models.primary_backup import PrimaryBackup
from models.secondary_backup import SecondaryBackup

class TestPrimaryBackup(unittest.TestCase):
    def setUp(self):
        image = Image("test_file.txt", "./tests/test_file.txt")

        replica_manager = SecondaryBackup(replica_manager_id=1, image=image)

        secondaries = {}
        secondaries[replica_manager.replica_manager_id] = replica_manager

        primary_backup = PrimaryBackup(replica_manager_id=0, image=image, secondaries=secondaries)

        self.action = primary_backup._check_all_secondary_health()

    def test_secondary_checks_out(self):
        self.assertEqual(self.action, {'status': True})


if __name__ == '__main__':
    unittest.main()
