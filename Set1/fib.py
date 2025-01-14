# Recursive function for Fibonacci sequence
def fibonacci_recursive(n):
    """Calculate the n-th Fibonacci number using recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative function for Fibonacci sequence
def fibonacci_iterative(n):
    """Calculate the n-th Fibonacci number using iteration."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update a and b
    return b

# Main program
def main():
    n = int(input("Enter the term (n) to find in the Fibonacci sequence: "))
    
    # Recursive approach
    print(f"Using recursion, the {n}-th Fibonacci number is: {fibonacci_recursive(n)}")
    
    # Iterative approach
    print(f"Using iteration, the {n}-th Fibonacci number is: {fibonacci_iterative(n)}")

if __name__ == "__main__":
    main()
