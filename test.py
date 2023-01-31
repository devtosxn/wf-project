import unittest
from user import User
from db import WafiDB

class Test(unittest.TestCase):
    def test_user_can_be_created(self):
        user = User("johndoe@gmail.com")
        db = WafiDB()
        db.add_user(user)
        self.assertEqual(user.email, "johndoe@gmail.com")
        self.assertEqual(len(db.users), 1)

    def test_user_can_retrieve_balance(self):
        user = User("john@gmail.com")
        self.assertEqual(user.balance, {"USD":0, "NGN":0, "GBP" : 0, "YUAN" : 0})
        self.assertEqual(user.check_balance(), "User - john@gmail.com balance - {'USD': 0, 'NGN': 0, 'GBP': 0, 'YUAN': 0}")
    
    def test_user_retrieves_correct_balance_after_deposit(self):
        user = User("jane@gmail.com")
        user.deposit_money(10, "USD")
        self.assertEqual(user.balance, {"USD":10, "NGN":0, "GBP" : 0, "YUAN" : 0})
  
    def test_user_retrieves_correct_balance_after_transfer(self):
        sender = User("sender@gmail.com")
        sender.deposit_money(25, "YUAN")
        receiver = User("receiver@gmail.com")
        sender.transfer_money(receiver.email, 10, "YUAN")
        self.assertEqual(sender.balance, {"USD":0, "NGN":0, "GBP" : 0, "YUAN" : 15})
        self.assertEqual(receiver.balance, {"USD":0, "NGN":0, "GBP" : 0, "YUAN" : 10})
        
    def test_user_retrieves_correct_balance_after_transfer_(self):
        sender = User("dominic@gmail.com")
        sender.deposit_money(4, "USD")
        sender.deposit_money(1245, "NGN")
        sender.deposit_money(50, "YUAN") 
        receiver = User("fred@gmail.com")                 
        sender.transfer_money(receiver.email, 5, "USD")
        self.assertIn(sender.balance, [{"USD":0, "NGN":830, "GBP" : 0, "YUAN" : 50}, {"USD":0, "NGN":1245, "GBP" : 0, "YUAN" : 41}])
        self.assertEqual(receiver.balance, {"USD":5, "NGN":0, "GBP" : 0, "YUAN" : 0})
    
    # def test_user_retrieves_correct_balance_after_withdrawal(self):
    #     user = User("test@gmail.com")
    #     user.deposit_money(10, "USD")
    #     user.withdraw_money(5, "USD")
    #     self.assertEqual(user.balance, {"USD":5, "NGN":0, "GBP" : 0, "YUAN" : 0})
