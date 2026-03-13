def count_subsets(arr, target):
    n = len(arr)

    # dp[i] = number of ways to make sum i
    dp = [0] * (target + 1)

    # base case
    dp[0] = 1

    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[target]


# Example
arr = [1, 2, 3, 3]
target = 6

print(count_subsets(arr, target))