def count_subsets_with_diff(arr, diff):
    total_sum = sum(arr)

    # Check if valid transformation exists
    if (diff + total_sum) % 2 != 0:
        return 0

    target = (diff + total_sum) // 2
    n = len(arr)

    dp = [0] * (target + 1)
    dp[0] = 1

    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[target]


# Example
arr = [1, 1, 2, 3]
diff = 1
print(count_subsets_with_diff(arr, diff))