

proceed = "yes"
while proceed == "yes":
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number: "))
    operator = input("Enter the operation you want to perform (e.g., +, -, *, /): ")

    # Calculations
    addition = number_one + number_two
    multiplication = number_one * number_two
    subtraction = number_one - number_two
    division = number_one / number_two

    # Output
    if operator == "+":
        print(f"The addition of the numbers is: {addition:.2f}")
    elif operator == "*":
        print(f"The multiplication of the numbers is: {multiplication:.2f}")
    elif operator == "-":
        print(f"The subtraction of the numbers is: {subtraction:.2f}")
    elif operator == "/":
        if number_two != 0:
             print(f"The division of the numbers is: {division:.2f}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid Input")
        
    proceed = input("Do you wnat to Proceed(Yes/No): ")


