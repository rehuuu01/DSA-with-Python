# Day 41 - Subset Sum (0/1 Knapsack Variation)

## Problem
Given an array and a target sum, determine if a subset exists whose sum equals the target.

## Pattern
This is a direct variation of 0/1 Knapsack.

State:
dp[i][j] -> Using first i elements, can we form sum j?

Transition:
If nums[i-1] <= j:
    dp[i][j] = dp[i-1][j] OR dp[i-1][j - nums[i-1]]
Else:
    dp[i][j] = dp[i-1][j]

## Complexity
Time: O(n * target)
Space: O(n * target)
Optimized Space: O(target)

## Key Learning
- Boolean DP table
- Reverse loop for space optimization
- Foundation for many DP problems