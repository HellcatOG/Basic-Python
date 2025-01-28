import random

def main():
    number_to_guess = random.randint(1, 100)
    guess_count = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1

        if user_guess < number_to_guess:
            print("Too low, try again.")
        elif user_guess > number_to_guess:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You've guessed the number in {guess_count} tries.")
            break


main()
