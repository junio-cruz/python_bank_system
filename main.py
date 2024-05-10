from typing import List


class Transaction:
    def __init__(self, transaction_type: str, amount: int):
        self.type = transaction_type
        self.amount = amount


balance = 0
withdraw_attempts = 3
withdraw_amount_limit = 500
extracts: List[Transaction] = []

start_menu = """
    [1] - Balance
    [2] - Deposit
    [3] - Withdraw
    [4] - Extract
    [5] - Exit
"""



def get_balance():
    print(f"Current balance: ", balance)

def deposit(amount: int):
    global balance
    balance += amount
    transaction = Transaction('deposit', amount)
    extracts.append(transaction)
    print("Deposit Success!")


def withdraw(amount: int):
    global balance
    if withdraw_attempts > 1:
        if balance < amount:
            print("Without balance!")
        elif withdraw_amount_limit <= 0:
            print("Withdraw amount daily limit reached!")
        else:
            balance -= amount
            transaction = Transaction('withdraw', amount)
            extracts.append(transaction)
            print("Withdraw Success!")
    else:
        print("Withdraw limit reached")


def get_extracts():
    for transaction in extracts:
        print(f"Transaction type: {transaction.type}, Amount: {transaction.amount}")


while True:
    option = int(input(start_menu))
    if option == 1:
        get_balance()
    if option == 2:
        deposit_amount = int(input("Insert amount for deposit:"))
        deposit(deposit_amount)
    elif option == 3:
        withdraw_amount = int(input("Insert amount for withdraw:"))
        withdraw(withdraw_amount)
    elif option == 4:
        get_extracts()
    elif option == 5:
        print("Thanks for use our system!")
