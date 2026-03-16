# Day 53 - Minimum Subset Sum Difference

Problem:
Given an array of positive integers, partition the array into two subsets such that the difference of their sums is minimized.

Approach:
This problem can be reduced to the Subset Sum pattern.

If total_sum is the sum of all elements, we try to find a subset with sum S1 closest to total_sum/2.

Difference = |total_sum - 2*S1|

We use a space optimized DP approach similar to subset sum.

Time Complexity: O(N * total_sum)
Space Complexity: O(total_sum)