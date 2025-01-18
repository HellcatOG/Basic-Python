# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


# Derived class for permanent employees
class PermanentEmployee(Employee):
    def __init__(self, name, salary, benefits):
        super().__init__(name, salary)
        self.benefits = benefits

    def calculate_salary(self):
        return self.salary  # Fixed salary

    def display_employee_info(self):
        super().display_employee_info()
        print(f"Benefits: {self.benefits}")


# Derived class for contract employees
class ContractEmployee(Employee):
    def __init__(self, name, salary, hourly_rate, hours_worked):
        super().__init__(name, salary)  # Base salary is set to 0 for contract employees
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"Hourly Rate: {self.hourly_rate}")
        print(f"Hours Worked: {self.hours_worked}")


# Example usage
permanent_employee = PermanentEmployee("Amit", 50000, "Health Insurance")
contract_employee = ContractEmployee("Sneha", 0, 30, 160)

print("Permanent Employee Info:")
permanent_employee.display_employee_info()

print("\nContract Employee Info:")
contract_employee.display_employee_info()

# Calculate and print the salaries
print("\nPermanent Employee Salary:", permanent_employee.calculate_salary())
print("Contract Employee Salary:", contract_employee.calculate_salary())
