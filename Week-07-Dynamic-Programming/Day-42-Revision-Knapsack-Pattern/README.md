# Day 42 – Knapsack Pattern Revision

## Overview

Day 42 was dedicated to revising the 0/1 Knapsack DP pattern and its variations.

Focus areas:
- Clear DP state definition
- Transition logic understanding
- Space optimization (1D DP reverse loop)
- Pattern mapping between related problems

## Problems Revised

- 0/1 Knapsack
- Subset Sum
- Equal Partition
- Count of Subsets with Given Sum

## Key Insight

All problems follow the same core structure:

dp[i][j] = answer using first i elements and target j

Only the transition operator changes:
- OR → Boolean problems
- +  → Counting problems
- max() → Maximization problems

Knapsack pattern reinforced ✔
Ready for advanced variations.