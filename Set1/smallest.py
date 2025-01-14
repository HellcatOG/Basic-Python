def smallest_number(num1, num2, num3):
    if num1 < num2:
        if num1 < num3:
            print(f"{num1} is the smallest number")
    elif num2 < num1:
        if num2 < num3:
            print(f"{num2} is the smallest number")
        elif num3 < num1:
            if num3 < num2:
                print(f"{num3} is the smallest number")
            
smallest_number(1, 0, 2)