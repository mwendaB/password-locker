from credetianls import Credential
from user import User

def create_user(firstname, lastname, password):
    new_user = User(firstname, lastname, password)
    return new_user

def save_user(user):
    User.save_user(user)

def 

