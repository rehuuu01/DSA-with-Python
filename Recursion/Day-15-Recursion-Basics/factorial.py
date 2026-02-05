def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
if __name__ == "__main__":
    n = int(input("Enter a non-negative integer to compute its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = fact(n)
        print(f"The factorial of {n} is: {result}")