import random
from typing import List


class Account:
    def __init__(self, name: str, password: str):
        self.user_name = name
        self.number = random.randint(0, 9999999)
        self.agency = random.randint(0, 9999)
        self.password = password
        self.extract: List[Transaction] = []
        self.balance = 0


class Transaction:
    def __init__(self, transaction_type: str, amount: int, account_number: int):
        self.type = transaction_type
        self.amount = amount
        self.account_number = account_number


current_account: Account
withdraw_attempts: int = 3
withdraw_amount_limit: int = 10000
accounts: List[Account] = []

start_menu = """
    [1] - Register Account
    [2] - Login Account
    [3] - Exit
"""

account_menu = """
    [1] - Balance
    [2] - Deposit
    [3] - Withdraw
    [4] - Extract
    [5] - Exit
"""


def get_account(account_agency: int, account_number: int):
    for account in accounts:
        if account.agency == account_agency and account.number == account_number:
            return account


def login_account():
    global current_account
    success: bool = False
    account_agency = int(input("Please, insert account agency:"))
    account_number = int(input("Please, insert account number:"))
    for account in accounts:
        if account.agency == account_agency and account.number == account_number:
            password = str(input("Please, insert password:"))
            if account.password == password:
                current_account = account
                print(f"================= LOGGED ACCOUNT ================= \n")
                print(f"Name: {current_account.user_name.upper()} \n"
                      f"Agency: {current_account.agency} \n"
                      f"Number: {current_account.number} \n"
                      f"Balance: {current_account.balance}")
                success = True
            else:
                print(f"================= WRONG PASSWORD ================= \n")
                break
        else:
            print(f"================= ACCOUNT NOT FOUND ================= \n")
    return success


def register_account():
    user_name = str(input("Please, insert account name:"))
    password = str(input("Please, insert password:"))
    account = Account(user_name, password)
    accounts.append(account)
    print(f"================= ACCOUNT CREATED ================= \n")
    print(f"Name: {account.user_name.upper()} \n"
          f"Agency: {account.agency} \n"
          f"Number: {account.number} \n"
          f"Balance: {account.balance}")


def get_balance():
    print(f"================= Current balance ================= \n", current_account.balance)


def deposit(amount: int):
    current_account.balance += amount
    transaction = Transaction('deposit', amount, current_account.number)
    current_account.extract.append(transaction)
    print(f"================= DEPOSIT SUCCESS ================= \n new balance: ", current_account.balance)


def withdraw(amount: int):
    global withdraw_attempts
    global withdraw_amount_limit
    if withdraw_attempts > 0:
        if current_account.balance < amount:
            print(f"================= WITHOUT BALANCE ================= \n balance: ", current_account.balance)

        elif withdraw_amount_limit <= 0:
            print(f"================= WITHDRAW AMOUNT LIMIT REACHED =================")
        else:
            current_account.balance -= amount
            withdraw_attempts -= 1
            withdraw_amount_limit -= amount
            transaction = Transaction('withdraw', amount, current_account.number)
            current_account.extract.append(transaction)
            print(f"================= WITHDRAW SUCCESS ================= \n new balance: ", current_account.balance)

    else:
        print(f"================= WITHDRAWAL ATTEMPT LIMIT REACHED =================")


def get_extract():
    print(f"================= Transactions ================= \n")
    for transaction in current_account.extract:
        print(f" {transaction.type.upper()} - {transaction.amount}")

    print(f"\n Balance:", current_account.balance)


def account_menu_options():
    global current_account
    while True:
        account_options = int(input(account_menu))
        if account_options == 1:
            get_balance()
        if account_options == 2:
            deposit_amount = int(input("Insert amount for deposit:"))
            deposit(deposit_amount)
        if account_options == 3:
            withdraw_amount = int(input("Insert amount for withdraw:"))
            withdraw(withdraw_amount)
        if account_options == 4:
            get_extract()
        elif account_options == 5:
            print("Thanks for use our system!")
            break


while True:
    options = int(input(start_menu))
    if options == 1:
        register_account()
        continue
    if options == 2:
        logged = login_account()
        if logged:
            account_menu_options()
        continue
    if options == 3:
        print("Thanks for use our system!")
        break
    else:
        print("Option not found!")
