from unittest.main import main
from user import User, Credentials

def create_new_user(username,password):
    new_user = User(username,password)
    return new_user

def save_user(user):
   
    user.save_user()
def display_user():
 
    return User.display_user()
def login_user(username,password):
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    credentials. save_details()
def display_accounts_details():
    return Credentials.display_credentials()

def delete_credential(credentials):
    credentials.delete_credentials()

def find_credential(account):
    return Credentials.find_credential(account)
def check_credendtials(account):
    return Credentials.if_credential_exist(account)

def generate_Password():
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    return Credentials.copy_password(account)


def main():
    print("Welcome to your Accounts Password locker...\n Please enter one of the following to proceed.\n ca ---  Create New Account  \n li ---  have an existing account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" ty - To type your own pasword:\n gen - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'ty':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gen':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*70)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*70)
    elif short_code == "li":
        print("*"*70)
        print("Enter your User name and your Password to log in:")
        print('*' * 100)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('\n')
    while True:
        print("Use these short codes:\n cc - Create a new credential \n disp - Display Credentials \n find - Find a credential \n gen - Generate A randomn password \n del - Delete credential \n ex - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" ty - To enter your own pasword if you already have an account:\n gen - To auto generate Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'ty':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gen':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "disp":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                 
                print('*' * 70)
                print('_'* 70)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 70)
                print('*' * 70)
            else:
                print("You don't have any credentials")
        elif short_code == "find":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 70)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 70)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "del":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*20)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your credentials for : {search_credential.account} deleted successfully.")
                print('\n')
            else:
                print("That Credential  does not exist")

        elif short_code == 'gen':

            password = generate_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using password locker.")
            break
        else:
            print("Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()