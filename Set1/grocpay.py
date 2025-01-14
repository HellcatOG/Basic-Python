work_hours = []
count = 0
try:
    for employee in range(1, 7):
        hours_worked = float(input(f"Enter Hours worked by employee {employee}: "))
        work_hours.append(hours_worked)
    

# Collect hourly rate

    hourly_rate = float(input("Hourly pay rate: "))
    

# Calculate and display gross pay for each employee
    for i in work_hours:
        count += 1
        salary = i * hourly_rate
        print(f"Gross pay for employee {count}: {salary}")
except ValueError:
    print("Please give interger Values")   
    




    


    