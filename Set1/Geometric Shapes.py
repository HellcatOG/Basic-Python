import math

# Circle-related functions
def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * (radius ** 2)

def circle_circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * math.pi * radius

# Rectangle-related functions
def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def rectangle_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

# Main program with menu
def main():
    while True:
        # Display menu
        print("\nMENU")
        print("1) Area of a circle")
        print("2) Circumference of a circle")
        print("3) Area of a rectangle")
        print("4) Perimeter of a rectangle")
        print("5) Quit")
        
        # Get user's choice
        choice = input("Enter your choice: ")

        if choice == "1":
            radius = float(input("Enter the circle's radius: "))
            print(f"The area is {circle_area(radius)}")
        elif choice == "2":
            radius = float(input("Enter the circle's radius: "))
            print(f"The circumference is {circle_circumference(radius)}")
        elif choice == "3":
            length = float(input("Enter the rectangle's length: "))
            width = float(input("Enter the rectangle's width: "))
            print(f"The area is {rectangle_area(length, width)}")
        elif choice == "4":
            length = float(input("Enter the rectangle's length: "))
            width = float(input("Enter the rectangle's width: "))
            print(f"The perimeter is {rectangle_perimeter(length, width)}")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()
