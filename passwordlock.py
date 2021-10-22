# run
import random
import string
from credetianls import User

def create_user(user_name,password):
    new_user = User(user_name,password)
    return new_user

def display_user():
    return User.display_user()

def del_user(user):
    user.delete_user()

def save_User(user):
    user.save_user()


def main():
    while True:
        print("Welcome to password lock")
        print('-'*60)
        print('\n')