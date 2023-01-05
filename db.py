class WafiDB:
    def __init__(self):
        self.users = {}

    def add_user(self, user:object):
        if user.email in self.users.keys():
            raise Exception("User with email {} already exists".format(user.email))
        self.users[user.email] = user
    
    def get_user(self, email:str):
        user = self.users.get(email, None)
        return user

    def list_users(self):
        return self.users