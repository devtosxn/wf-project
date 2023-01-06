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
        self.assertEqual(user.balance, 0)
        self.assertEqual(user.check_balance(), "User - john@gmail.com has $0")
    
    def test_user_retrieves_correct_balance_after_deposit(self):
        user = User("jane@gmail.com")
        user.deposit_money(10)
        self.assertEqual(user.balance, 10)
  
    def test_user_retrieves_correct_balance_after_transfer(self):
        sender = User("sender@gmail.com")
        sender.deposit_money(20)
        receiver = User("receiver@gmail.com")
        sender.transfer_money(receiver.email, 10)
        self.assertEqual(sender.balance, 10)
        self.assertEqual(receiver.balance, 10)
    
    def test_user_retrieves_correct_balance_after_withdrawal(self):
        user = User("test@gmail.com")
        user.deposit_money(10)
        self.assertEqual(user.balance, 10)
