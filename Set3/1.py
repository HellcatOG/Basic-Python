class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
         
    def print_info(self):
        print(f"{self.firstname} {self.lastname}")
        
    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self, fname, lname, age, student_id, major):
        super().__init__(fname, lname, age)
        self.student_id = student_id
        self.major = major

    # Exercise 3: Override the print_info method
    def print_info(self):
        super().print_info()
        print(f"ID: {self.student_id}")
        
    def student_age_check(self):
        if self.age >= 18:
            return "an adult"
        else:
            return "not an adult"
            
    def print_student_info(self):
        print(f"Full Name: {self.get_full_name()}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"Age Status: {self.student_age_check()}")


class PartTimeStudent(Student):
    def __init__(self, fname, lname, age, student_id, major, hours_per_week):
        super().__init__(fname, lname, age, student_id, major)
        self.hours_per_week = hours_per_week
    
    # Exercise 4: Check if part-time or full-time
    def is_full_time(self):
        return self.hours_per_week >= 20

    def print_info(self):
        super().print_info()
        if not self.is_full_time():
            print(f"{self.get_full_name()} is a part-time student.")
        else:
            print(f"{self.get_full_name()} is a full-time student.")


class Employee(Person):
    def __init__(self, fname, lname, age, employee_id, department, salary):
        super().__init__(fname, lname, age)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    # Exercise 3: Override the print_info method
    def print_info(self):
        super().print_info()
        print(f"Employee ID: {self.employee_id}")
        
    # Exercise 5: Calculate annual salary
    def get_annual_salary(self):
        return self.salary * 12


# Testing the classes

# Exercise 3: Testing Student print_info override
student = Student("John", "Doe", 20, "S12345", "Computer Science")
student.print_info()  # Expected: "John Doe, ID: S12345"

# Exercise 4: Testing PartTimeStudent class
part_time_student = PartTimeStudent("John", "Doe", 20, "S12345", "Computer Science", 15)
part_time_student.print_info()  # Expected: "John Doe is a part-time student."

# Exercise 5: Testing Employee annual salary calculation
employee = Employee("Jane", "Smith", 25, "E7890", "Human Resources", 5000)
employee.print_info()  # Expected: "Jane Smith, Employee ID: E7890"
print(f"Annual Salary: {employee.get_annual_salary()}")  # Expected: 60000
