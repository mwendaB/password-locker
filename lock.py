import unittest
import pyperclip
from user import User
from credetianls import Credential

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Brian', 'Mwenda', 'mwendaB')



    def test_init_(self):
        self.assertEqual(self.new_user.first_name, 'Brian')
        self.assertEqual(self.new_user.last_name, 'Mwenda')
        self.assertEqual(self.new_user.password, 'mwendaB')
