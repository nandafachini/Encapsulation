# Implement the AccountBanking and Customer classes, 
# as shown in the class diagram below.

# -------------------------------------               ----------------------
# | AccountBanking                    |               | Client             |
# -------------------------------------               ----------------------
# | + number: int                     |               | + name: str        |
# | + client: Client                  |---------------| + id: str          |
# | - balance: float                  |               | - password: str    |
# -------------------------------------               ----------------------
# | + get_balance()                   |               | + get_password()   |
# | + deposit(value, password)        |               ----------------------
# | + withdraw_money(value, password) |
# -----------------------------------

#  the sign "+" indicates public attribute or method
#  the sign "-" indicates private attribute or method

# get_balance(): return account balance.

# deposit(): receives as input parameters a value and a password. 
# Adds this amount to the account balance only if the password is 
# the same as the customer's password.

# withdraw_money(): receives as input parameters a value and a password. 
# Subtract this amount from the account balance, only if the password is 
# the same as the customer's password.


class Client:
    def __init__(self, name, id, password):
        self.name = name
        self.__id = id
        self.__password = password

    def get_balance(self):
        return self.__password


class AccountBanking:
    def __init__(self, number, client):
        self.number = number
        self.client = client
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, value, password):
        if password == self.client.get_balance():
            self.__balance += value
        else:
            print("Incorrect password")

    def withdraw_money(self, value, password):
        if password == self.client.get_balance():
            self.__balance -= value
        else:
            print("Incorrect password")

client1 = Client("João", "111111111", "123")
account = AccountBanking(1111, client1)

print(account.get_balance())            # Prints 0
account.deposit(200, "123")
print(account.get_balance())            # Prints 200
account.withdraw_money(50, "123")
print(account.get_balance())            # Prints 150

account.deposit(100, "111")             # Incorrect password
print(account.get_balance())            # Prints 150
account.withdraw_money(50, "111")       # Incorrect password
print(account.get_balance())            # Prints 150

