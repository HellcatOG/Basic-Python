#attadance tracker
present_students = ""

while True:
    student_name = input("Enter the name of a present student (enter 'end' to stop): ") #input
    if student_name == 'end':
        break
    present_students += student_name + "\n"  
print("List of students: ") #output
print(present_students)
