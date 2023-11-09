from atm import BankAccount, User

users = [
    User("Hello", 24, "Nothing 1"),
    User("World", 10, "Nothing 2"),
]

accounts = [
    BankAccount("12345", users[0], 1000.0),
    BankAccount("67890", users[1], 500.0),
]

exported = {
    'users': users,
    'accounts': accounts
}