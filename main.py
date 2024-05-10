from typing import List


class Transaction:
    def __init__(self, transaction_type: str, amount: int):
        self.type = transaction_type
        self.amount = amount


balance: int = 0
withdraw_attempts: int = 3
withdraw_amount_limit: int = 10000
extracts: List[Transaction] = []

start_menu = """
    [1] - Balance
    [2] - Deposit
    [3] - Withdraw
    [4] - Extract
    [5] - Exit
"""


def get_balance():
    print(f"================= Current balance ================= \n", balance)

def deposit(amount: int):
    global balance
    balance += amount
    transaction = Transaction('deposit', amount)
    extracts.append(transaction)
    print(f"================= DEPOSIT SUCCESS ================= \n new balance: ", balance)


def withdraw(amount: int):
    global balance
    global withdraw_attempts
    global withdraw_amount_limit
    if withdraw_attempts > 0:
        if balance < amount:
            print(f"================= WITHOUT BALANCE ================= \n balance: ", balance)

        elif withdraw_amount_limit <= 0:
            print(f"================= WITHDRAW AMOUNT LIMIT REACHED =================")
        else:
            balance -= amount
            withdraw_attempts -= 1
            withdraw_amount_limit -= amount
            transaction = Transaction('withdraw', amount)
            extracts.append(transaction)
            print(f"================= WITHDRAW SUCCESS ================= \n new balance: ", balance)

    else:
        print(f"================= WITHDRAWAL ATTEMPT LIMIT REACHED =================")


def get_extracts():
    global balance
    print(f"================= Transactions ================= \n")
    for transaction in extracts:
        print(f" {transaction.type.upper()} - {transaction.amount}")

    print(f"\n Balance:", balance)


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
        break
    else:
        print("Option not found!")

