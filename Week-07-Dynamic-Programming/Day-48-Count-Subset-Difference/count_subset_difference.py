def count_subsets_with_diff(nums, diff):
    total_sum = sum(nums)

    # If transformation not possible
    if (diff + total_sum) % 2 != 0:
        return 0

    target = (diff + total_sum) // 2

    # DP array
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[target]


# Example
nums = [1, 1, 2, 3]
diff = 1

print(count_subsets_with_diff(nums, diff))