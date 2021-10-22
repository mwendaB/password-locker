import unittest
import pyperclip
from user import User
from credetianls import Credential

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Brian', 'Mwenda', 'mwendaB')
