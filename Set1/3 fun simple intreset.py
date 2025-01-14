

def cal_interest(balance, interest_rate):
    interest = balance * (interest_rate / 100)
    return interest

def balance_update(balance, interest):
    new_balance = balance + interest
    return new_balance

def main():
    balance = int(input("Enter your balance: "))
    interest_rate = int(input("Enter your Intrest rate: "))
    intrest1 = cal_interest(balance,interest_rate)
    balance = balance_update(balance, intrest1)
    print(f"Updated balance is {balance}")



main()
    
