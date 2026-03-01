def findTargetSumWays(nums, target):
    total_sum = sum(nums)
    
    # Edge case
    if total_sum < abs(target) or (total_sum + target) % 2 != 0:
        return 0
    
    subset_sum = (total_sum + target) // 2
    
    # DP array
    dp = [0] * (subset_sum + 1)
    dp[0] = 1
    
    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]
    
    return dp[subset_sum]


# Example usage
nums = [1, 1, 1, 1, 1]
target = 3
print(findTargetSumWays(nums, target))  # Output: 5