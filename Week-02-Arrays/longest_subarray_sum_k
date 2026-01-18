def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    max_length = 0
    prefix_index = {}  # stores first occurrence of prefix_sum

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Case 1: subarray from 0 to i has sum = k
        if prefix_sum == k:
            max_length = i + 1

        # Case 2: subarray between two indices has sum = k
        if (prefix_sum - k) in prefix_index:
            length = i - prefix_index[prefix_sum - k]
            max_length = max(max_length, length)

        # Store prefix_sum only if not already present
        if prefix_sum not in prefix_index:
            prefix_index[prefix_sum] = i

    return max_length


# Main execution block
if __name__ == "__main__":
    arr = list(map(int, input(
        "Enter the elements of the array separated by spaces: "
    ).split()))
    k = int(input("Enter value of K: "))

    print("Length of longest subarray with sum K:",
          longest_subarray_sum_k(arr, k))
