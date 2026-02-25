# recursive.py

def knapsack_recursive(weights, values, W, n):
    """
    0/1 Knapsack - Recursive Approach
    
    Time Complexity: O(2^n)
    Space Complexity: O(n) (recursion stack)
    """
    
    # Base Case
    if n == 0 or W == 0:
        return 0
    
    # If current item's weight exceeds capacity
    if weights[n - 1] > W:
        return knapsack_recursive(weights, values, W, n - 1)
    
    # Include or Exclude
    include = values[n - 1] + knapsack_recursive(
        weights, values, W - weights[n - 1], n - 1
    )
    exclude = knapsack_recursive(weights, values, W, n - 1)
    
    return max(include, exclude)


# Example Usage
if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    W = 7
    n = len(weights)
    
    result = knapsack_recursive(weights, values, W, n)
    print("Maximum Value (Recursive):", result)