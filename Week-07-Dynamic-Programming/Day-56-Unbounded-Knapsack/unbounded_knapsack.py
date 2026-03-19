def unbounded_knapsack(weights, values, W):
    """
    Unbounded Knapsack (1D DP - Space Optimized)

    :param weights: List[int]
    :param values: List[int]
    :param W: int (capacity)
    :return: int (maximum value)
    """
    n = len(weights)

    # DP array
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(weights[i], W + 1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[W]


# Example usage
if __name__ == "__main__":
    weights = [2, 4, 6]
    values = [5, 11, 13]
    W = 10

    result = unbounded_knapsack(weights, values, W)
    print("Maximum Value:", result)