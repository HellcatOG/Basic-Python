class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        area = (3.14* radius)^2
        return area
        
    def circumfrence(self):
        circumfrence = (2 *3.14)* radius
        return circumfrence
    
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"Cirdum is {circle.circumfrence()}")






        