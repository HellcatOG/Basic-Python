class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __str__(self):
        return f"{self.fname} {self.lname}"
        
        
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
        
        
            
            
            
person1 = Person("Jhon", "Abhrham")
person2 = Student("Pranav","Unnikrishnan")
print(person1)
print(person1, person2.graduationyear)

