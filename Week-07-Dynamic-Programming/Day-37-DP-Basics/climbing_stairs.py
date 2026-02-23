"""
Day 37 - Dynamic Programming Basics
Climbing Stairs Problem

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb either 1 step or 2 steps.
Return the number of distinct ways to reach the top.

This problem follows the Fibonacci pattern.
"""


# -------------------------------------------------
# 1️⃣ Recursive Solution (Exponential - O(2^n))
# -------------------------------------------------
def climb_recursive(n):
    """
    Recursive solution.
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n
    return climb_recursive(n - 1) + climb_recursive(n - 2)


# -------------------------------------------------
# 2️⃣ Memoization (Top-Down DP)
# -------------------------------------------------
def climb_memo(n, dp=None):
    """
    Memoization approach.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if dp is None:
        dp = [-1] * (n + 1)

    if n <= 2:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = climb_memo(n - 1, dp) + climb_memo(n - 2, dp)
    return dp[n]


# -------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# -------------------------------------------------
def climb_tab(n):
    """
    Tabulation approach.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# -------------------------------------------------
# 4️⃣ Space Optimized (Best Version)
# -------------------------------------------------
def climb_optimized(n):
    """
    Space optimized approach.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 2:
        return n

    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# -------------------------------------------------
# Example Usage
# -------------------------------------------------
if __name__ == "__main__":
    n = 5

    print("Recursive:", climb_recursive(n))
    print("Memoization:", climb_memo(n))
    print("Tabulation:", climb_tab(n))
    print("Space Optimized:", climb_optimized(n))