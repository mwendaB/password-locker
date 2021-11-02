import unittest
from passwordlock import User, Credentials



class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Brian', 'MwendaB')


    def test_init(self):
        self.assertEqual(self.new_user.username, 'Brian')
        self.assertEqual(self.new_user.password, 'MwendaB')


    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)

    # def test_save_multiple_user(self): 
       
    #     self.new_user.save_user()
    #     test_user = User("Eugine", "Abongo", "fozar") 
    #     test_user.save_user()
    #     self.assertEqual(len(User.users_list), 2)
    
    # def test_delete_user(self): 
    #     self.new_user.save_user()
    #     test_user = User("Eugine", "Abongo", "fozar") 
    #     test_user.save_user()
    #     self.new_contact.delete_contact()
    #     self.assertEqual(len(User.contact_list), 1) 



class TestCredentials(unittest.TestCase):


    def setUp(self):
        self.new_credential = Credentials('Email', 'Brian', 'MwendaB' )

    def test_init(self):
        self.assertEqual(self.new_credential.account, 'Email')
        self.assertEqual(self.new_credential.userName, 'Brian')
        self.assertEqual(self.new_credential.password,'MwendaB')
    
    
    def save_credential_test(self):
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        Credentials.credentials_list = []


    def test_save_many_accounts(self):
        self.new_credential.save_details()
        test_credential = Credentials("Instagram","Eugine","fozar") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
   
     
    
    def test_delete_credential(self):
        self.new_credential.save_details()
        test_credential = Credentials("Instagram","Eugine","fozar")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_find_credentials(self):
        self.new_credential.save_details()
        test_credential = Credentials("Instagram","Eugine","fozar") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("Instagram")

        self.assertEqual(the_credential.account,test_credential.account)

    def test_credential_exist(self):
        self.new_credential.save_details()
        the_credential = Credentials("Instagram", "Eugine", "fozar")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Instagram")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()