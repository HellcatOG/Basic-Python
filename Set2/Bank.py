class BankAccount:
    def __init__(self,account_holder ):
        self.account_holder = account_holder
        self.balance = 0
        
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amounbt must me grater than 0")
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdarwed {amount}. New balance:{self.balance}")
        else:
            print("Insufficent fund")
    
    def display_balance(self):
        print(f"balance:{self.balance}")

account_holder =  input("enter account holder name: ")
account = BankAccount(account_holder)
account.deposit(5000)
account.withdraw(1000)
account.display_balance