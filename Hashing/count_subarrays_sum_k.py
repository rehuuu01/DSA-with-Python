def count_subarrays_with_sum_k(arr, k):
    prefix_sum = 0
    count = 0
    prefix_count = {0: 1}  # stores frequency of prefix_sum

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Check if there is a prefix_sum that when subtracted from current
        # prefix_sum gives k
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]

        # Update the frequency of the current prefix_sum
        if prefix_sum in prefix_count:
            prefix_count[prefix_sum] += 1
        else:
            prefix_count[prefix_sum] = 1

    return count
if __name__ == "__main__":
    arr = list(map(int, input(
        "Enter the elements of the array separated by spaces: "
    ).split()))
    k = int(input("Enter value of K: "))

    print("count of subarrays with sum K:", count_subarrays_with_sum_k(arr, k))






