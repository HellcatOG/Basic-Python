class Book:
    def __init__(self, Name, Author, Year):
        self.Name = Name
        self.Author = Author
        self.Year = Year
        
#     def display_books(self):
#         return f"{self.Name}, {self.Author}, {self.Year}"

    def __str__(self):
        return f"{self.Name}, {self.Author}, {self.Year}"
    
    def myfun(self):
        print("The Book is " +self.Name)
        
y1 = Book("Wings", "Salvin", "2024")
y2 = Book("Nike", "Ragna", "2024")

print(y1)
print(y2)
y1.myfun()
