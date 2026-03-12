# Day 50 – Partition with Given Difference

## Problem
Count the number of ways to partition an array into two subsets such that the difference of their sums equals a given value.

## Key Idea
Using the equations:

subset1 + subset2 = totalSum  
subset1 - subset2 = diff  

We derive:

subset1 = (totalSum + diff) / 2

Thus the problem reduces to counting subsets with sum = (totalSum + diff) / 2.

## Approach
Dynamic Programming – 0/1 Knapsack Pattern (Count Subset Sum).

## Complexity
Time Complexity: O(N × Target)  
Space Complexity: O(Target)