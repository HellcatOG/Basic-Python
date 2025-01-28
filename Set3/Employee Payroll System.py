def calculate_salary(basic_pay, allowance, deduction):
    gross_pay = (basic_pay + allowance) 
    if gross_pay > 5000:
        tax = gross_pay * 0.1
    else:
        tax = 0
    net_salary = gross_pay - deduction - tax
    return net_salary

def main():
    basic_pay = int(input("Enter basic pay: "))
    allowance = int(input("Enter allowances: "))
    deduction = int(input("Enter deduction: "))
    
    result = calculate_salary(basic_pay, allowance, deduction)
    print(f"Net Salary: {result}")

main()
