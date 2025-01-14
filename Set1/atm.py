current_balance = 1000 
print("Welcome to Atm")
print(f"Current Balance: ${current_balance} ")

while True:
    withdraw = float(input("Enter amount to withdraw (enter 0 to exit): "))
    if withdraw == 0:
        print("Exiting the ATM. Have a nice day!")
        break
    elif withdraw > current_balance:
        print("Error: Insufficient funds")
    elif withdraw % 10 != 0:
        print("Error: Amount must be a multiple of $10.")
    elif withdraw <= current_balance:
        new_balance = current_balance - withdraw
        current_balance = new_balance
        print(f"Withdrawal successful. New balance: ${new_balance}")
    else:
        print("Invaild Input")
        


