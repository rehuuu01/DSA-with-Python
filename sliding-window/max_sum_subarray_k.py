def max_sum_subarray_k(arr, k):
    if len(arr) < k or k <= 0:
        return None  # Edge case: not enough elements or invalid k

    max_sum = float('-inf')
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add the next element to the window

        # Slide the window when we hit the size k
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)  # Update max sum if needed
            window_sum -= arr[window_start]  # Remove the element going out of the window
            window_start += 1  # Slide the window ahead

    return max_sum
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter the size of subarray (k): "))
    # Call the function and print the result
    result = max_sum_subarray_k(arr, k)
    if result is None:
       print("Invalid input")
    else:
       print(f"The maximum sum of a subarray of size {k} is: {result}")
