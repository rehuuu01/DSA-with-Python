# Day 47 — Unbounded Knapsack

Today's topic continues the Dynamic Programming journey with the **Unbounded Knapsack pattern**.

Unlike the 0/1 Knapsack problem, each item can be chosen multiple times.

Problem Solved
--------------
Unbounded Knapsack

Key Idea
--------
For every item, we can reuse it multiple times while the remaining capacity allows.

State
-----
dp[w] → Maximum value achievable with capacity w

Transition
----------
dp[w] = max(dp[w], value[i] + dp[w - weight[i]])

Complexity
----------
Time Complexity: O(n * W)
Space Complexity: O(W)

This pattern is commonly used in problems like Coin Change and Rod Cutting.