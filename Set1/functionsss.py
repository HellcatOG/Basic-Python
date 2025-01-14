def main():
    intro()
    cup = int(input("Enter the number of cups: "))
    cups_to_ounces(cup)
    
def intro():
    print("""This program converts measurements in cups to fluid ounces. For your refreance the formula is:
1 cup = 8 fluid ounces""")
    
def cups_to_ounces(cup):
    ounces = cup * 8
    print(f" {cup} cup is = {ounces} fulid ounces")
    
main()