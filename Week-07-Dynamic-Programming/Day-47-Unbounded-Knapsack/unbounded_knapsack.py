def unbounded_knapsack(weights, values, W):
    n = len(weights)

    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(weights[i], W + 1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[W]


# Example
weights = [2, 3, 4]
values = [40, 50, 60]
W = 8

print("Maximum Value:", unbounded_knapsack(weights, values, W))