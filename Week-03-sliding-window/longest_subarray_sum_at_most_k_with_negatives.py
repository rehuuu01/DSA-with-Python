# Works for negative + positive numbers

def longest_subarray_sum_at_most_k(arr, k):
    prefix_sum = 0
    max_length = 0

    # Stores earliest index of each prefix sum
    prefix_index = {0: -1}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Check all previous prefix sums
        for prev_sum in prefix_index:
            if prefix_sum - prev_sum <= k:
                max_length = max(max_length, i - prefix_index[prev_sum])

        # Store earliest occurrence only
        if prefix_sum not in prefix_index:
            prefix_index[prefix_sum] = i

    return max_length


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter the sum limit (k): "))

    result = longest_subarray_sum_at_most_k(arr, k)
    print(f"The length of the longest subarray with sum at most {k} is: {result}")
