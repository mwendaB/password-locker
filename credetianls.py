class Credential:
    
    
    credentials_list = []

    def __init__(self, user_name, social_media, account_name, password):
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
    def confirm_user(cls, first_name, password):
        
        active_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                active_user = user.first_name
        return active_user