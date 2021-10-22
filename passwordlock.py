from credetianls import Credential
from user import User

def create_user(firstname, lastname, password):
    new_user = User(firstname, lastname, password)
    return new_user

def save_user(user):
    User.save_user(user)

def  delete_user(user):
    user.delete_User()

def authenticate_user(first_name, password):
     confirm_user = Credential.confirm_user(first_name, password)
     return confirm_user

def generate_password():
    generate_password = Credential.generate_password()
    return generate_password


def create_credential(user_name, social_media, account_name, password):
    
    new_credential = Credential(
        user_name, social_media, account_name, password)
    return new_credential 
