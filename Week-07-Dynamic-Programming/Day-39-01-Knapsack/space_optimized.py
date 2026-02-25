# space_optimized.py

def knapsack_optimized(weights, values, W):
    """
    0/1 Knapsack - Space Optimized Version
    
    Time Complexity: O(n * W)
    Space Complexity: O(W)
    """
    
    n = len(weights)
    dp = [0] * (W + 1)
    
    for i in range(n):
        # Traverse backwards to prevent overwriting needed values
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )
    
    return dp[W]


# Example Usage
if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    W = 7
    
    result = knapsack_optimized(weights, values, W)
    print("Maximum Value (Space Optimized):", result)