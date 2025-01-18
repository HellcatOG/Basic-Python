numbers = []
count = int(input("enter the numbers: "))
for i in range(count):
    num = int(input("enter the numbers: "))
    numbers.append(num)
print("The max is: ",max(numbers))