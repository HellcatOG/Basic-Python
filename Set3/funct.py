class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
         
    def print_info(self):
        print(self.firstname, self.lastname)
        print(f"Age: {self.age}")
        
    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"
    
    
class Student(Person):
    def __init__(self, fname, lname, age, student_id, major):
        super().__init__(fname, lname, age)
        self.student_id = student_id
        self.major = major
    
    def print_info(self):
        super().print_info()
        print(f"Student ID: {self.student_id}")
        
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
        print(f"Adult : {self.get_full_name()} is {self.student_age_check()}")
        

class Employee(Person):
    def __init__(self, fname, lname, age, employee_id, department):
        super().__init__(fname, lname, age)
        self.employee_id = employee_id
        self.department = department
        
    def print_info(self):
        super().print_info()
        print(f"Employee ID: {self.employee_id}")
        
    def employee_age_check(self):
        if self.age >= 18:
            return "an adult"
        else:
            return "not an adult"
    

    def print_employee_info(self):
        print(f"Name: {self.get_full_name()}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Adult: {self.get_full_name()} is {self.employee_age_check()}")
        
    def employee_age_check(self):
        if self.age >= 18:
            return "an adult"
        else:
            return "not an adult"


student = Student("John", "Doe", 20, "S12345", "Computer Science")
student.print_student_info()

employee = Employee("Jane", "Smith", 45, "E7890", "Human Resources")
employee.print_employee_info()
