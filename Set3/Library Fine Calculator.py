def calculate_fine(days_overdue):
    if days_overdue <= 0:
        return 0
    elif days_overdue <= 5:
        return days_overdue * 1
    elif days_overdue <= 15:
        return (5 * 1) + ((days_overdue - 5) * 2)
    else:
        return (5 * 1) + (10 * 2) + ((days_overdue - 15) * 5)

def main():
    days = int(input("Enter the number of days the book is overdue: "))
    fine = calculate_fine(days)
    print(f"The fine amount is: {fine}")

main()
