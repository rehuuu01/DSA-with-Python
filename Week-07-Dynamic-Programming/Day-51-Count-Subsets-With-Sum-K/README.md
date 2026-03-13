# Day 51 — Count Subsets With Sum K

## Problem
Given an array of integers and a target value K, count the number of subsets whose sum equals K.

Example:
Input: arr = [1,2,3,3], K = 6  
Output: 3

Subsets:
[1,2,3]
[1,2,3]
[3,3]

## Approach

This is a variation of the **0/1 Knapsack pattern**.

We use **Dynamic Programming** where:

dp[j] = number of ways to achieve sum j

Transition:

dp[j] += dp[j - num]

We iterate backwards to prevent reuse of the same element.

## Complexity

Time Complexity: O(N × K)  
Space Complexity: O(K)