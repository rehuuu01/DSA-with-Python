# Day 43 - Target Sum (0/1 Knapsack Variation)

## Problem
Given an array and a target value, count the number of ways to assign + or - signs to reach the target.

## Key Insight
Convert the problem to:
Count subsets with sum = (total_sum + target) // 2

## Approach
- Check edge cases
- Convert to subset sum count problem
- Use space-optimized DP

## Time Complexity
O(n * target)

## Space Complexity
O(target)