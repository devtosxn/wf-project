from user import User, get_system_overview

get_system_overview()

user_1 = User("johndoe@gmail.com")
user_1.deposit_money(10, "NGN")

user_2 = User("janedoe@gmail.com")
user_2.deposit_money(20, "USD")

user_2.transfer_money("johndoe@gmail.com", 15, "USD")

user_1.withdraw_money(amount=25)

get_system_overview()