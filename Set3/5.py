class Person:
    person_count = 0

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        Person.person_count += 1

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    @staticmethod  #anottaion
    def get_person_count():
        return Person.person_count


class Student(Person):
    def __init__(self, fname, lname, student_id, major):
        super().__init__(fname, lname)
        self.student_id = student_id
        self.major = major


class PartTimeStudent(Student):
    def __init__(self, fname, lname, student_id, major, hours_per_week):
        super().__init__(fname, lname, student_id, major)
        self.hours_per_week = hours_per_week

    def is_full_time(self):
        return self.hours_per_week >= 20

    def print_info(self):
        status = "full-time" if self.is_full_time() else "part-time"
        print(f"{self.get_full_name()} is a {status} student.")


class Employee(Person):
    def __init__(self, fname, lname, employee_id, department, salary):
        super().__init__(fname, lname)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12

    def print_employee_info(self):
        print(f"{self.get_full_name()}'s annual salary is {self.get_annual_salary()}")



person1 = Person("John", "Doe")
student1 = Student("Alice", "Johnson", "S001", "Mathematics")
employee1 = Employee("Jane", "Smith", "E123", "Engineering", 5000)


print(f"Total Persons: {Person.get_person_count()}")
