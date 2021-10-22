class Credential:
    
    
    credentials_list = []

    def __init__(self, user_name, social_media, account_name, password):
       
        self.user_name = user_name
        self.social_media = social_media
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        Credential.credentials_list.append(self)
