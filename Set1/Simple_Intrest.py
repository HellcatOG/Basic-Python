#input

principle_amount = float(input("Enter the principle amount: "))
intrest_rate = float(input("Enter the annuel intrest rate(eg: 6 for 6): "))
total_years =int(input("Enter the number of Years: "))

#calculations

simple_intrest = principle_amount*(intrest_rate/100)*total_years

#Display
print(f"Simple Intrest is: {simple_intrest:.2f}")
