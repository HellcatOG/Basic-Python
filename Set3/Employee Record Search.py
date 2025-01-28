
def find_employee_by_id(employee_data, employee_id):
    for employee in employee_data:
        if employee_id == employee[0]:
            print(employee[1])
        else:
            continue
                
employee_data = employee_data = [(101, 'Alice', 'HR'), (102, 'Bob', 'IT'), (103, 'Charlie', 'Finance')]
employee_id= 102

result = find_employee_by_id(employee_data, employee_id)
print(result)
    







