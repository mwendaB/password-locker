# accoun
class User:
    user_list =[]


    def __init__(self, user_name,password):
        self.user_name = user_name
        self.password = password


 
    def save_user(self):
        
        '''
        A method that save an instance of a user in the user list
        '''
        User.user_list.append(self)


    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        return cls.user_list