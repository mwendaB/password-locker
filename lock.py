# cred

import random
import string

class Credentials:
    Credentials_list = []
    def __init__ (self, account_username, account_password):
        self.account_username = account_username
        self.account_password = account_password