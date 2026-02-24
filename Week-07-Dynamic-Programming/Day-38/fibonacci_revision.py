# -------------------------------------------------
# 1️⃣ Simple Recursion (Inefficient - O(2^n))
# -------------------------------------------------
def fib_recursive(n):
    """
    Returns nth Fibonacci number using plain recursion.
    Time Complexity: O(2^n)
    Space Complexity: O(n) (recursion stack)
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# -------------------------------------------------
# 2️⃣ Memoization (Top-Down DP) - O(n)
# -------------------------------------------------
def fib_memo(n, dp=None):
    """
    Returns nth Fibonacci number using memoization.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if dp is None:
        dp = [-1] * (n + 1)

    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib_memo(n - 1, dp) + fib_memo(n - 2, dp)
    return dp[n]


# -------------------------------------------------
# 3️⃣ Tabulation (Bottom-Up DP) - O(n)
# -------------------------------------------------
def fib_tab(n):
    """
    Returns nth Fibonacci number using tabulation.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# -------------------------------------------------
# 4️⃣ Space Optimized Version - O(n) time, O(1) space
# -------------------------------------------------
def fib_optimized(n):
    """
    Returns nth Fibonacci number using space optimization.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n

    prev2 = 0  # F(0)
    prev1 = 1  # F(1)

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# -------------------------------------------------
# Example Usage
# -------------------------------------------------
if __name__ == "__main__":
    n = 10

    print("Recursive:", fib_recursive(n))
    print("Memoization:", fib_memo(n))
    print("Tabulation:", fib_tab(n))
    print("Space Optimized:", fib_optimized(n))