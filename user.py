import pyperclip
import string
import random


class User:
    user_list = []
    def __init__(self, username, password):
       
        self.username = username
        self.password = password
    
    def save_user(self):
        User.user_list.append(self)
    
    def delete_user(self):
        User.user_list.remove(self)

  
    @classmethod
    def display_user(cls):
       
        return cls.user_list


class Credential:
    
    
    credentials_list = []
    @classmethod
    def verify_user(cls,username, password):
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

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





