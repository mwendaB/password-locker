import unittest
from credetianls import User


class TestUser(unittest.TestCase):



    def SetUp(self):
        self.new_account =User("Brian","mwenda")
    
    def test_init(self):
        self.assertEqual(self.new_account.user_name, "Brian")
        self.assertEqual(self.new_account.password, "mwenda")
    