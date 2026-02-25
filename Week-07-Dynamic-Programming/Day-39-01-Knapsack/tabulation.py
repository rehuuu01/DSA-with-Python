# tabulation.py

def knapsack_tabulation(weights, values, W):
    """
    0/1 Knapsack - Tabulation (Bottom-Up DP)
    
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    """
    
    n = len(weights)
    
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]


# Example Usage
if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    W = 7
    
    result = knapsack_tabulation(weights, values, W)
    print("Maximum Value (Tabulation):", result)