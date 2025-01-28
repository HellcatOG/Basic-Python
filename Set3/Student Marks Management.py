top_students = []
def get_top_students(student_marks, threshold):
    for student, marks in student_marks.items():
        if marks > threshold:
            top_students.append(student)
        else:
            continue
    return top_students

def main():        
    student_marks = {'John': 75, 'Emily': 88, 'Tom': 60, 'Anna': 93}
    threshold = 70

    result = get_top_students(student_marks, threshold)
    print(f"Students scoring above {threshold}:", result)

main()
            