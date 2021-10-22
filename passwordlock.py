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

