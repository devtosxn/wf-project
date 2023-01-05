from db import WafiDB

db = WafiDB()

class User:
    def __init__(self, email:str):
        self.email = email
        self.balance = 0
        db.add_user(self)

    def check_balance(self):
        return f"User - {self.email} has ${self.balance}"

    def deposit_money(self, amount:int):
        self.balance += amount

    def transfer_money(self, receiver_email:str, amount:int):
        if self.balance < amount:
            raise Exception("Insufficient funds")
        receiver = db.get_user(receiver_email)
        if not receiver:
            raise Exception("User not found")
        
        self.balance -= amount
        receiver.balance += amount
        
    def withdraw_money(self, amount):
        if self.balance < amount:
            raise Exception("Insufficient funds")
        self.balance -= amount
    

def get_system_overview():
    users = db.list_users()
    print("WAFI SYSTEM OVERVIEW")
    if not users: 
        print("No users in System")
        print("END OF SYSTEM OVERVIEW")
        return
    for user in users:
            print(f"User - {user} has ${users[user].balance}")
    print("END OF SYSTEM OVERVIEW")


    