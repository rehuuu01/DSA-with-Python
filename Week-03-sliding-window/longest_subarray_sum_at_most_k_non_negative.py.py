def longest_subarray_sum_at_most_k(arr, k):
    n = len(arr)
    max_length = 0
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += arr[right]

        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter the sum limit (k): "))
    # Call the function and print the result
    result = longest_subarray_sum_at_most_k(arr, k)
    print(f"The length of the longest subarray with sum at most {k} is: {result}")