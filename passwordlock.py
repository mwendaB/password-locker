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
        print("To create a new user account use 'ca': To login to your account use: 'lg': To delete user use: 'dl' To display user use: 'di' To exit use: 'ex'")
        short_code =input().lower()
        print('\n')



        if short_code == 'ca':
            print("create username")
            created_user_name = input()
            print("Want sytem to generate passowrd? 'y' or 'n'")
            yes = input()
            if yes == "y": 
                pass_code = string.ascii_letters
                create_password = "".join(random.choice(pass_code) for i in range(10)) 
                print("pasword Generated!!!") 
                continue       