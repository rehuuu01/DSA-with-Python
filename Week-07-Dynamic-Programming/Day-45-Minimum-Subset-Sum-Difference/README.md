# Day 45 - Minimum Subset Sum Difference

## Problem
Given an array of integers, divide it into two subsets such that the absolute difference between their sums is minimized.

## Approach
This problem is solved using the Subset Sum dynamic programming pattern.

Let total sum = S.

If subset sum is s1, the other subset sum will be S - s1.

The difference becomes:

|S - 2*s1|

We compute all possible subset sums up to S//2 using DP and find the minimum difference.

## Complexity

Time Complexity: O(n × S)  
Space Complexity: O(S)