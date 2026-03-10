# Day 48 — Count Subsets With Given Difference

## Problem
Given an array of integers and a difference `diff`, count the number of subsets such that the difference between subset sums equals `diff`.

## Key Idea
Let:
sum1 - sum2 = diff  
sum1 + sum2 = totalSum

Adding both equations:

2 * sum1 = diff + totalSum

Therefore:

sum1 = (diff + totalSum) / 2

This converts the problem into counting the number of subsets with sum = target.

## Approach
1. Compute total sum of array.
2. Transform problem into subset sum.
3. Use Dynamic Programming to count subsets.

## Complexity
Time: O(n * target)  
Space: O(target)