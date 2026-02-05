def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Sum is not defined for negative numbers.")
    else:
        print(f"The sum of the first {n} numbers is: {sum_n(n)}")
