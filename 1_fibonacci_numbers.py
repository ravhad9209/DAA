def recursive_fibonacci(n):
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 1:
        return n
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# Main program
if __name__ == "__main__":
    n = int(input("Enter Your number :"))
    print("Fibonacci sequence:")
    for i in range(n):
        print(recursive_fibonacci(i))
    

# def non_recursive_fibonacci(n):
#     first = 0
#     second = 1

#     print("Fibonacci sequence:")
#     for i in range(n):
#         print(first)
#         # Update the two previous numbers
#         next_num = first + second
#         first = second
#         second = next_num

# # Main program
# if __name__ == "__main__":
#     n = int(input("Enter the number of terms: "))
#     non_recursive_fibonacci(n)