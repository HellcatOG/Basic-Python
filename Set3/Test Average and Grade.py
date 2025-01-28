def calc_average(score1, score2, score3, score4, score5):
   
    return (score1 + score2 + score3 + score4 + score5) / 5

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():

    scores = []
    for i in range(1, 6):
        score = float(input(f"Enter test score {i}: "))
        scores.append(score)

    
    print("\nTest Scores and Grades:")
    for i, score in enumerate(scores, start=1):
        grade = determine_grade(score)
        print(f"Test {i}: {score} - Grade: {grade}")

    
    average_score = calc_average(*scores)
    average_grade = determine_grade(average_score)
    print(f"\nAverage Test Score: {average_score:.2f} - Grade: {average_grade}")


main()
