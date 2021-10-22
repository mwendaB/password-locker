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
        print("To create a new user account use 'ca': To login to your account use: 'lg': To delete user use: 'del' To display user use: 'disp' To exit use: 'ex'")
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
                print("password Generated!!!") 
                continue       

            else:
                print("create password")
                create_password = input()

                print("confirm password")
                confirm_password = input()

            
            while create_password != confirm_password:
                print("Password dont match")
                print("Enter your password")
                create_password = input()
                confirm_password = input()
            else:
              print(f"Welcome {user_name_entered}.Login was successful")
        

        elif short_code == 'lg':
            print("welcome")
            print("Enter user name")
            default_user_name = input()

            print("enter password")
            default_password = input()
            print('\n')

            while default_user_name != 'mwendaB' or default_password !='00000':
                print("Wrong user name or password. Username 'mwendaB' and password '00000' ")
                print("enter username")
                default_user_name =input()
                print("enter password")
                default_password = input()
                print('\n')

            else:
                print("login Success")
                print('\n')
                print("-"*30)

        elif short_code == 'disp':
            if display_user():
                 print("Here is a list of all your users")
                 print('\n')
                 for user in display_user():
                     print(f"{user.user_name}")
                     print('\n')

            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'del':
            print("Want to delete account? 'y' 'n'")
            yes = input()
            if yes == 'y':
                del_user()
                print("Deleted successfully")
            else:
                print("Account not found") 

        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")

