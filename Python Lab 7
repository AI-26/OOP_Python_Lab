class ATM:
    def __init__(self, account_number, balance=0):
        # Initialize ATM account with account number and balance
        self.account_number = account_number
        self.balance = balance



class ATM:
    def __init__(self, account_number, balance=0):
        # Initialize ATM account with account number and balance
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        """Function to check the current balance"""
        print(f"Current balance: ${self.balance}")

    def deposit(self, amount):
        """Function to deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Function to withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def transfer(self, other_atm, amount):
        """Function to transfer money to another ATM account"""
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds for transfer.")
        else:
            self.balance -= amount
            other_atm.balance += amount
            print(f"Transferred ${amount} to account {other_atm.account_number}.")
            print(f"New balance: ${self.balance}")
            print(f"Recipient's new balance: ${other_atm.balance}")


# Example Usage
atm1 = ATM(account_number="12345", balance=1000)
atm2 = ATM(account_number="67890", balance=500)

atm1.check_balance()  # Check balance of atm1
atm1.deposit(200)  # Deposit into atm1
atm1.withdraw(150)  # Withdraw from atm1
atm1.transfer(atm2, 300)  # Transfer money to atm2
atm2.check_balance()  # Check balance of atm2





