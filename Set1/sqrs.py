inp = int(input("Enter the Number limit: "))
print("Number \t Square")
print("--------------")
for x in range(1, inp+1):
    y = x**2
    print(f"{x} \t {y}")