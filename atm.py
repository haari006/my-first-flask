class User(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_address(self, new_address):
        self.address = new_address
        return f'Address updated successfully.'

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Address: {self.address}'


class BankAccount(object):

    def __init__(self, account_number, user: User, balance=0.0):
        self.account_number = account_number
        self.user = user
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f'Deposited {amount} successfully. New balance: {self.balance}'

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f'Withdrawn {amount} successfully. New balance: {self.balance}'
        else:
            return 'Insufficient funds. Withdrawal failed.'

    def get_balance(self):
        return f'Current balance: {self.balance}'

    def __str__(self):
        return f'Account Number: {self.account_number}, User: {self.user.name}, Balance: {self.balance}'


