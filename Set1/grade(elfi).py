#input

marks = float(input("Enter your total Marks: "))

#Calculations

if marks >= 90:
    print("Your grade is A")
elif marks >=80:
        print("Your grade is B")
elif marks >= 70:
        print("Your grade is C")
elif marks >= 60:
        print("Your grade is D")
elif marks >= 50:
        print("Your grade is E")
else:
    print("You have failed")