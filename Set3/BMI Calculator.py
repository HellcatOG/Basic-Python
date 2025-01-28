def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    
    
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obesity"
    
    return bmi, status


def main():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi, status = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Health status: {status}")

main()
