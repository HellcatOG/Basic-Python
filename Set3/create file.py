f = open("sales.txt", "w")

days_count = int(input("Enter the number of days: "))

for i in range(1, days_count + 1):
    sales = input(f"Enter sales for day {i}: ")
    f.write(f"Sales of day {i}: {sales}\n")

f.close()
print("Data written to sales.txt")



















