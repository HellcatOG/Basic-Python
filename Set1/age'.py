#Input

age = int(input("Enter your age: "))

#

if age <= 13:
    print("You are a Child")
elif age <= 20:
    print("You are a Teenager")
elif age <= 59:
    print("You are an Adult")
elif age >= 60:
    print("You are a Senior")
else:
    print("Invalid Input")
