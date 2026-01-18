def missing_number_xor(arr):
    n = len(arr)
    xor_all = 0

    # XOR all numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i

    # XOR all elements of the array
    for num in arr:
        xor_all ^= num

    return xor_all


# Main execution block
if __name__ == "__main__":
    arr = list(map(int, input(
        "Enter the elements of the array separated by spaces: "
    ).split()))

    print("The missing number is:", missing_number_xor(arr))

