num_students = int(input("How many students do you have? "))
num_tests = int(input("How many test scores per student? "))


for student in range(1, num_students + 1):
    print(f"\nStudent number {student}")
    print("-----------------")
    
    total_score = 0
    for test in range(1,num_tests + 1):
        score = float(input(f"Test number {test}: "))
        total_score += score
        
    average_score = total_score / num_tests
    print(f"The average for student number {student} is: {average_score:.1f}")