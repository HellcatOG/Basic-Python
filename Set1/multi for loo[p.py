number = int(input("Enter a number: "))
last_number = int(input("Enter the range of needed: "))

for x in range(1, last_number + 1):
    table = number * x
    print(f"{x} * {number} = {table}")