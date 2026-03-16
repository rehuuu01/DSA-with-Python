def min_subset_sum_difference(arr):
    total_sum = sum(arr)
    n = len(arr)

    dp = [False] * (total_sum + 1)
    dp[0] = True

    for num in arr:
        for j in range(total_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    min_diff = float('inf')

    for s1 in range(total_sum // 2 + 1):
        if dp[s1]:
            diff = abs(total_sum - 2 * s1)
            min_diff = min(min_diff, diff)

    return min_diff


arr = [1, 6, 11, 5]
print(min_subset_sum_difference(arr))