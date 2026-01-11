def count_digits(n):
    #display 1 when n is 0
    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Number of digits:", count_digits(abs(n)))
    # Use abs(n) to handle negative numbers correctly