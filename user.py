import pyperclip 
import string
import random


class User:
    user_list = []
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def save_user(self):
        User.user_list.append(self)
    
    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def confirm_user(cls, first_name, password):
        
        active_user = ''
        for user in cls.user_list:
            if (user.first_name == first_name and user.password == password):
                active_user = user.first_name
        return active_user



class Credential:
    
    
    credentials_list = []

   
    def __init__ (self, user_name, social_media, account_name, password):
        self.user_name = user_name
        self.social_media = social_media
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        Credential.credentials_list.append(self)
    
    def generate_password():
        pwchar = string.printable
        length = int(input('Enter password length desired: '))
        generate_password = ''
        for pwchar in range(length):
            generate_password += random.choice(pwchar)
        return generate_password

    
 
 

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
    
    @classmethod
    def search_social_media(cls, social_media):
        
        for credential in cls.credentials_list:
            if credential.social_media == social_media:
                return credential
    
    @classmethod 
    def copy_password(cls, social_media):
       
        collect_password = Credential.search_social_media(social_media)
        return pyperclip.copy(collect_password.password) 





