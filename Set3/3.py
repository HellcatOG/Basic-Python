class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"


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



part_time_student = PartTimeStudent("John", "Doe", "S12345", "Computer Science", 15)
part_time_student.print_info()
