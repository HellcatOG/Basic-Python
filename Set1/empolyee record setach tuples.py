employee_data = [(101, 'Alice', 'HR'), (102, 'Bob', 'IT'), (103, 'Charlie', 'Finance')]


def employee(data):
    employee_id= int(input("Enter the epmloyee ID: "))
    for i in employee_data:
        if employee_id == i[0]:
            print(i[1])
               
employee(employee_data)