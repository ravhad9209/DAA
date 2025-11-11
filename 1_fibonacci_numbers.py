# Recursive Fibonacci with step count
steps = 0  # Global variable to count steps

def recursive_fibonacci(n):
    global steps
    steps += 1  # Count each function call
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Non-recursive (iterative) Fibonacci with step count
def non_recursive_fibonacci(n):
    steps = 0
    a, b = 0, 1
    print("Fibonacci sequence (Iterative):")
    for i in range(n):
        print(a)
        steps += 1
        a, b = b, a + b
    print("Total steps (iterations):", steps)

# Main program
if __name__ == "__main__":
    n = int(input("Enter number of terms: "))

    # Recursive version
    steps = 0  # Reset step counter
    print("\nFibonacci sequence (Recursive):")
    for i in range(n):
        print(recursive_fibonacci(i))
    print("Total recursive steps (function calls):", steps)

    # Iterative version
    print("_"*30)
    non_recursive_fibonacci(n)
