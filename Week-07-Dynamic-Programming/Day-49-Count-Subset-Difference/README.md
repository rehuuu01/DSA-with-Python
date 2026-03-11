# Day 49 - Count of Subsets with Given Difference

## Problem
Given an array and a difference `diff`, count the number of subsets such that:

subset1 - subset2 = diff

## Key Idea
Using equations:

S1 - S2 = diff  
S1 + S2 = total_sum  

Adding both:

2S1 = diff + total_sum

Therefore:

S1 = (diff + total_sum) / 2

The problem reduces to counting subsets with sum = S1.

## Approach
Dynamic Programming (0/1 Knapsack pattern) using space optimized DP.

## Time Complexity
O(n * target)

## Space Complexity
O(target)