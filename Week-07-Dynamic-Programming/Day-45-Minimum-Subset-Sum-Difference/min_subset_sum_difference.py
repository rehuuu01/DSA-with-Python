def min_subset_sum_difference(nums):
    total_sum = sum(nums)
    n = len(nums)

    target = total_sum // 2

    # DP array
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    min_diff = float("inf")

    for s1 in range(target + 1):
        if dp[s1]:
            diff = abs(total_sum - 2 * s1)
            min_diff = min(min_diff, diff)

    return min_diff


# Example
nums = [1, 6, 11, 5]
print("Minimum Subset Sum Difference:", min_subset_sum_difference(nums))