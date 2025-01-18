class car:
    def __init__(self, make, model, year, fuel_level = 100):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        
    def drive(self, distance):
        fuel_consumed = distance * 0.1
        self.fuel_level -= fuel_consumed
        print(f"Driving {distance} km. Fuel level: {self.fuel_level}%")
        
    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level >=100:
            self.fuel_level = 100
        print(f"Refueled {amount}%. Fuel level: {self.fuel_level}%")
        
    def status(self):
        print( f"{self.year} {self.make} {self.model} - Fuel level: {self.fuel_level}%")
        
car1 = car("BMW", "M4", 2026)
car1.drive(100)
car1.refuel(10)
car1.status()
        
        
        