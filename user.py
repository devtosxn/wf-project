from db import WafiDB

db = WafiDB()
market_rates = { "USD": 1, "NGN" : 415, "GBP":0.86, "YUAN" : 6.89}

def convert_curr(from_curr, to_curr, amt):
    return ((amt * market_rates[to_curr])/market_rates[from_curr])


class User:
    def __init__(self, email:str):
        self.email = email
        self.balance = {"USD":0, "NGN":0, "GBP" : 0, "YUAN" : 0}
        db.add_user(self)

    def check_balance(self):
        return f"User - {self.email} balance - {self.balance}"

    def deposit_money(self, amount:int, currency:str):
        self.balance[currency] += amount

    def transfer_money(self, receiver_email:str, amount:int, currency:str):
        receiver = db.get_user(receiver_email)
        if not receiver:
            raise Exception("User not found")

        if self.balance[currency] < amount:
            deficient_amt = amount - self.balance[currency] 

            alt_curr = [curr for curr in self.balance.keys() if curr != currency] 
            alt_amts = {curr:convert_curr(curr, currency, self.balance[curr]) for curr in alt_curr}
            
            if sum(alt_amts.values()) < deficient_amt: #This means there is no deductable amount in the alt balances to cover the deficient amount
                raise Exception("Insufficient funds")
            
            elif max(alt_amts.values()) >= deficient_amt: #This means there is surely a deductable amount from one of the alt balances to cover the deficient amount                
                for key, amt in alt_amts.items():
                    if amt >= deficient_amt:
                        self.balance[key] -= convert_curr(currency, key, deficient_amt)
                        break
                self.balance[currency] = 0
            else: #This means we can remove the deficient amount from the sum of alt balances, clear the initial balance and then add balance to it
                balance = sum(alt_amts.values()) - deficient_amt
                self.balance[currency] = balance
            
            receiver.balance[currency] += amount

        else:
            self.balance[currency] -= amount
            receiver.balance[currency] += amount

    # def withdraw_money(self, amount, currency):
    #     if self.balance < amount:
    #         raise Exception("Insufficient funds")
    #     self.balance -= amount
    

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


    