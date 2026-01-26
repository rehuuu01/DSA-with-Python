def print_1_to_n(n):
    if n <= 0:
        return
    print_1_to_n(n - 1)
    print(n)
if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    print(f"Printing numbers from 1 to {n}:")
    print_1_to_n(n)
