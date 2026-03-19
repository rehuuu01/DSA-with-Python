# Day 56 – Unbounded Knapsack

## 📌 Problem
Given weights and values of items, maximize value with capacity W.
Each item can be taken multiple times.

## 🧠 Key Idea
Unlike 0/1 Knapsack:
- We can reuse same item → stay in same row

Transition:
dp[i][w] = max(dp[i-1][w], value + dp[i][w - weight])

## ⚡ Optimized
1D DP possible

## ⏱ Complexity
Time: O(N * W)
Space: O(W)