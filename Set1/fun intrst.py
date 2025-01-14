def main():
    principal = int(input("Enter the princile amount: "))
    period = int(input("enter the period: "))
    rate = float(input("Enter the intrest rate: "))
    show_intrest(rate, period, principal)
    
def show_intrest(rate, period, principal):
    simple_intrest = principal* rate *period
    print(f"The simple intrest is: {simple_intrest}")

main()
    