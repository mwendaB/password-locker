import unittest
from credetianls import User


class TestUser(unittest.TestCase):



    def SetUp(self):
        self.new_account =User("Brian","mwenda")
    
    def test_init(self):
        self.assertEqual(self.new_account.user_name, "Brian")
        self.assertEqual(self.new_account.password, "mwenda")
    
    def test_save_user(self):
        self.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_delete_user(self):
        self.delete_user()
        self.assertEqual(len(User.user_list), 0)
    