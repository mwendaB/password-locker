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


    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_user(self): 
       
        self.new_user.save_user()
        test_user = User("Eugine", "Abongo", "fozar") 
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2)
    
    def test_delete_user(self): 
        self.new_user.save_user()
        test_user = User("Eugine", "Abongo", "fozar") 
        test_user.save_user()
        self.new_contact.delete_contact()
        self.assertEqual(len(User.contact_list), 1) 



class TestCredentials(unittest.TestCase):


    def test_confirm_user(self):
        
        self.new_user = User('Brian', 'Mwenda', 'mwendaB')
        self.new_user.save_user()
        userX = User('Brian', 'Mwenda', 'mwendaB')
        userX.save_user()
        active_user = Credential.confirm_user('Brian', 'mwendaB')
        self.assertTrue(active_user)
    
    def setUp(self):
       
        self.new_credential = Credential(
            'Eugine', 'Instagram', 'Abongo', 'fozar')


    def test__init__(self):
        self.assertEqual(self.new_credential.user_name, 'Eugine')
        self.assertEqual(self.new_credential.social_media, 'Instagram')
        self.assertEqual(self.new_credential.account_name, 'Abongo')
        self.assertEqual(self.new_credential.password, 'fozar')

    def test_save_credentials(self):
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 1)

    def tearDown(self):
        User.users_list = []
        Credential.credentials_list = []




