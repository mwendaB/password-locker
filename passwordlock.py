from user import User
from credetianls import Credential


def create_user(firstname, lastname, password):
    new_user = User(firstname, lastname, password)
    return new_user


def save_user(user):
    User.save_user(user)


def delete_user(user):  
    user.delete_user()


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


def save_credential(credential):
    Credential.save_credentials(credential)


def display_credentials():
    return Credential.display_credentials()


def copy_password(social_media):
    return Credential.copy_password(social_media)


def main():
		print('')
		print('Welcome to Password Locker.')
		print('')
		print(' ')
		while True:
			print(' ')
			print("-"*70)
			print('Navigation Commands: \n ca-Create Password Locker Account \n li-Log Into Password Locker to access your credentials \n ex- To exit')
			short_code = input('Enter an option: ').lower().strip()
			if short_code == 'ex':
				break

			elif short_code == 'ca':
				print("-"*70)
				print(' ')
				print('To create a new password locker account:')
				first_name = input('Enter your first name - ').strip()
				last_name = input('Enter your last name - ').strip()
				password = input('Enter your password - ').strip()
				save_user(create_user(first_name, last_name, password))
				print(" ")
				print(
					f'A new Password Locker Account Created for: {first_name} {last_name} which will be accessed using this password: {password}')
			elif short_code == 'li':
				print("-"*70)
				print(' ')
				print('To login, enter your password locker account details:')
				user_name = input('Enter your first name - ').strip()
				password = str(input('Enter your password - '))
				user_exits = authenticate_user(user_name, password)
				if user_exits == user_name:
					print(" ")
					print(f'{user_name} Please choose an option to continue.')
					print(' ')
					while True:
						print("-"*70)
						print('Navigation commands: \n cs-Create Social Media credentials\n disp-Display Credentials \n copy-Copy Social Media Password \n ex- To exit')
						short_code = input('Choose an option: ').lower().strip()
						print("-"*70)
						if short_code == 'ex':
							print(" ")
							print(f'Goodbye {user_name}')
							break
						elif short_code == 'cc':
							print(' ')
							print('Enter your credential details:')
							social_media = input('Enter the social media name- ').strip()
							account_name = input('Enter your social media handle - ').strip()
							while True:
								print(' ')
								print("-"*70)
								print('Please choose an option for entering a password: \n pas-enter existing password \n gen-generate a password \n ex- To exit')
								psw_options = input('Enter an option: ').lower().strip()
								print("-"*70)
								if psw_options == 'pas':
									print(" ")
									password = input('Enter your password: ').strip()
									break
								elif psw_options == 'gen':
									password = generate_password()
									break
								elif psw_options == 'ex':
									break
								else:
									print('Oops! Incorrect option entered. Please try again.')
							save_credential(create_credential(
								user_name, social_media, account_name, password))
							print(' ')
							print(
								f'Credential Created: social media Name: {social_media} - Social Media Handle: {account_name} - Password: {password}')
							print(' ')
						elif short_code == 'disp':
							print(' ')
							if display_credentials():
								print('Here is a list of all your social media credentials')
								print(' ')
								for credential in display_credentials():
									print(
										f'Social Media Account: {credential.social_media} - Social Media Handle: {credential.account_name} - Password: {credential.password}')
								print(' ')
							else:
								print(' ')
								print("Sorry, we didn't find any credentials. cc which is create credential to add.")
								print(' ')
						elif short_code == 'copy':
							print(' ')
							choose = input(
								'Enter the social_media name for the credential password to copy: ')
							copy_password(choose)
							print('Password copied succesfully')
						else:
							print('Sorry! Incorrect option entered. Try again.')

				else:
					print(' ')
					print('Sorry! Incorrect details entered. Try again or Create an Account.')

			else:
				print("-"*70)
				print(' ')
				print('Sorry! Incorrect option entered. Try again.')


if __name__ == '__main__':
	main()