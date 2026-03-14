# Day 52 – Dynamic Programming Revision (0/1 Knapsack Pattern)

## Topics Revised

This revision focuses on strengthening the **0/1 Knapsack DP pattern**, particularly the subset transformation problems solved in previous days.

### Problems Reviewed

1. Subset Sum
2. Equal Partition
3. Count of Subsets with Given Sum
4. Target Sum
5. Minimum Subset Sum Difference
6. Count Subsets With Given Difference
7. Partition With Given Difference
8. Count Subsets With Sum K

## Key Idea

Most of these problems reduce to a **Subset Sum DP table**.

State Definition:

dp[i][j] → number of ways to form sum `j` using first `i` elements.

Transition:

If arr[i-1] <= j

dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]

Else

dp[i][j] = dp[i-1][j]

## Goal of this Revision

- Strengthen recognition of the **0/1 Knapsack pattern**
- Understand how different problems transform into **subset sum**
- Improve confidence with **DP table reasoning**

This revision helps build a strong foundation before moving to the next DP patterns.