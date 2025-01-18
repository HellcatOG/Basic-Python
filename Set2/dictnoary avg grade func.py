def calulate_average(grade, threshold):
    total = 0
    count = 0
    for x in grade.values():
        if x < threshold:
            continue
        else:
            count += 1
            total += x
    average = total/count
    return average

grades = {'Alice':85, 'Bob':30, 'Charlie':72, 'David':55}
result = calulate_average(grades, 40)
print(result)