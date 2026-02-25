# memoization.py

def knapsack_memo(weights, values, W, n, dp):
    """
    0/1 Knapsack - Memoization (Top-Down DP)
    
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    """
    
    if n == 0 or W == 0:
        return 0
    
    if dp[n][W] != -1:
        return dp[n][W]
    
    if weights[n - 1] > W:
        dp[n][W] = knapsack_memo(weights, values, W, n - 1, dp)
    else:
        include = values[n - 1] + knapsack_memo(
            weights, values, W - weights[n - 1], n - 1, dp
        )
        exclude = knapsack_memo(weights, values, W, n - 1, dp)
        dp[n][W] = max(include, exclude)
    
    return dp[n][W]


# Example Usage
if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    W = 7
    n = len(weights)
    
    dp = [[-1] * (W + 1) for _ in range(n + 1)]
    
    result = knapsack_memo(weights, values, W, n, dp)
    print("Maximum Value (Memoization):", result)