def count_partitions_with_diff(arr, diff):
    total_sum = sum(arr)

    # Edge case
    if (total_sum + diff) % 2 != 0:
        return 0

    target = (total_sum + diff) // 2

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

print(count_partitions_with_diff(arr, diff))