class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def print_info(self):
        print(self.get_full_name())


class Student(Person):
    def __init__(self, fname, lname, student_id, major):
        super().__init__(fname, lname)
        self.student_id = student_id
        self.major = major

    def print_info(self):
        super().print_info()
        print(f"ID: {self.student_id}")


class Employee(Person):
    def __init__(self, fname, lname, employee_id, department):
        super().__init__(fname, lname)
        self.employee_id = employee_id
        self.department = department

    def print_info(self):
        super().print_info()
        print(f"ID: {self.employee_id}")



student = Student("John", "Doe", "S12345", "Computer Science")
employee = Employee("Jane", "Smith", "E54321", "Marketing")


student.print_info()  
employee.print_info()  
