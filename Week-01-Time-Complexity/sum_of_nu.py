def sum_of_n(n):
    # Formula approach (most efficient)
    return n * (n + 1) // 2


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    if n < 0:
        print("Please enter a non-negative number")
    else:
        print("Sum of first", n, "numbers:", sum_of_n(n))
    # # Iterative approach (less efficient)