def min_size_subarray_sum(arr, target):
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += arr[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    target = int(input("Enter the target sum: "))
    # Call the function and print the result
    result = min_size_subarray_sum(arr, target)
    print(f"The minimum size of a subarray with sum at least {target} is: {result}")