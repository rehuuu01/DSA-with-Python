def count_occurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    target = int(input("Enter element to count: "))
    # Call the function and print the result
    result=count_occurrences(arr, target)
    # Print the result
    print(f"The element {target} occurs {result} times in the array.")