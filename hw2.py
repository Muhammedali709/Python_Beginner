import datetime
import random

class BankAccount:

    def __init__(self):
        self.accounts = {}
        print("Welcome to BANK. You can create a BankAccount, withdraw, and deposit money from your bank account!")

    def create_account(self):
        name = input("Enter your Name and Surname: ")
        while True:
            birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
            try:
                birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        age = datetime.datetime.now().year - birthdate.year - ((datetime.datetime.now().month, datetime.datetime.now().day) < (birthdate.month, birthdate.day))
        password = input("Enter the password: ")
        
        if age<18:
            print("Bank accounts are prohibited for people under 18!")
        else:
            account_id = random.randint(100000,999999) 
            self.accounts[account_id] = {'name': name, 'balance': 0, 'password': password,'account_id':account_id,'transactions':[]} 
            print(f"Account created successfully for {name}.")
            print(f"Your id is {account_id}. Do not forget your id, it will be required for processes.")
            return account_id

    def login(self):
        account_id = int(input("Enter your account ID: "))
        password = input("Enter your Password: ")
        if account_id in self.accounts and self.accounts[account_id]['password'] == password:
            print(f"Welcome {self.accounts[account_id]['name']}!")
            return account_id
        else:
            print("Incorrect ID or password!")
            return None


    def personal_inform(self,account_id):
        
        print(f"Name: {self.accounts[account_id]['name']}\nID: {self.accounts[account_id]['account_id']}\nBalance: {self.accounts[account_id]['balance']}$")
    def balance_check(self, account_id):
        if account_id in self.accounts:
            print(f"Your current balance is: {self.accounts[account_id]['balance']}$")
        else:
            print("Account not found.")

    def deposit(self,account_id):
        if account_id in self.accounts:
            amount = int(input("Enter the amount to deposit: ")) 
            self.accounts[account_id]['balance'] += amount
            self.accounts[account_id]['transactions'].append(f"Deposit-{amount}$")
            print(f"Deposited {amount}. New balance is {self.accounts[account_id]['balance']}$.")
        else:
            print("Account not found.")

    def withdraw(self,account_id):  
        if account_id in self.accounts:
            amount = int(input("Enter the amount to withdraw: "))
            self.accounts[account_id]['transactions'].append(f"Withdraw-{amount}$")
            if amount > self.accounts[account_id]['balance']:
                print("Insufficient balance")
            else:
                self.accounts[account_id]['balance'] -= amount
                print(f"Withdrew {amount}. New balance is {self.accounts[account_id]['balance']}$.")
        else:
            print("Account not found.")
    def transaction_history(self,account_id):
        if account_id in self.accounts:
            print("The transaction history :")
            for i in self.accounts[account_id]['transactions']:
                print(i)
        else:
            print("Account not found")        
        



bank_account = BankAccount()

    
while True:
    print("""
    1. CREATE AN ACCOUNT
    2. LOG IN
    0. EXIT
    """)
        
    a = input("Select the process: ")

        
    if a=='1':
        bank_account.create_account()
    elif a== '2':
        account_id = bank_account.login()
        if account_id:
            while True:
                process = input("Enter 1 to check balance, 2 to deposit, 3 to withdraw,4 to see personal information,5 to see the transactions history, 0 to logout: ")
                if process=='1':
                    bank_account.balance_check(account_id)
                elif process=='2':
                    bank_account.deposit(account_id)
                elif process=='3':
                    bank_account.withdraw(account_id)
                elif process=='4':
                    bank_account.personal_inform(account_id)
                elif process=='5':
                    bank_account.transaction_history(account_id)    
                elif process=='0':
                    break
                else:
                    print("Invalid option. Please try again.")
    elif a=='0':
        break
    else:
        print("Incorrect input. Please try again.")
