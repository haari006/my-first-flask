from flask import Flask
from atm import User, BankAccount
from flask import request

from models import accounts, users

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    user1 = User(name, 24, "Earth")
    return user1.__str__()


@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.json
    user1 = User(user_data["name"], user_data["age"], user_data["address"])

    account_number = user_data.get("account_number")
    account1 = BankAccount(account_number, user1, user_data.get("balance", 0.0))

    return ({
        'user': user1.__str__(),
        'account': account1.__str__()
    })


@app.route('/account/<account_number>/deposit', methods=['POST'])
def deposit_atm(account_number):
    account = next((acc for acc in accounts if acc.account_number == account_number), None)

    if account:
        response = account.deposit(request.json["amount"])
        return {'response': f'{response} for user {account.user.name}'}, 200
    else:
        return ({'error': 'Account not found'}), 404


@app.route('/account/<account_number>/withdraw', methods=['POST'])
def withdraw_atm(account_number):
    account = next((acc for acc in accounts if acc.account_number == account_number), None)

    if account:
        response = account.withdraw(request.json["amount"])
        return {'response': f'{response} for user {account.user.name}'}, 200
    else:
        return ({'error': 'Account not found'}), 404


@app.route('/account/<account_number>/balance', methods=['GET'])
def get_balance(account_number):
    account = next((acc for acc in accounts if acc.account_number == account_number), None)

    if account:
        response = account.get_balance()
        return {'response': f'{response} for user {account.user.name}'}, 200
    else:
        return ({'error': 'Account not found'}), 404


@app.route('/users', methods=['GET'])
def get_users():
    return {'users': [user.__str__() for user in users]}, 200


@app.route('/users/<name>/address', methods=['POST'])
def update_address(name):
    user = next((user for user in users if user.name == name), None)

    if user:
        user.update_address(request.json["address"])
        return {'response': f'Address updated successfully for user {user.name}'}, 200
    else:
        return ({'error': 'User not found'}), 404
