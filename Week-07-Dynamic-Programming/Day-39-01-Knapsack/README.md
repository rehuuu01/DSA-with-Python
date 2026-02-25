# Day 39 – 0/1 Knapsack Problem

## 📌 Problem Statement

Given:
- `n` items
- `weights[]`
- `values[]`
- Knapsack capacity `W`

Select items such that:
- Total weight ≤ W
- Total value is maximized
- Each item can be taken at most once (0/1 choice)

---

## 🧠 Approaches Implemented

### 1️⃣ Recursive (Brute Force)
- Try all combinations (include / exclude)
- Time Complexity: O(2^n)
- Space Complexity: O(n) recursion stack

### 2️⃣ Memoization (Top-Down DP)
- Store overlapping subproblems in DP table
- Time Complexity: O(n * W)
- Space Complexity: O(n * W)

### 3️⃣ Tabulation (Bottom-Up DP)
- Build DP table iteratively
- Time Complexity: O(n * W)
- Space Complexity: O(n * W)

### 4️⃣ Space Optimized
- Use 1D DP array
- Traverse capacity backwards
- Time Complexity: O(n * W)
- Space Complexity: O(W)

---

## 📊 DP State Definition

Let:

dp[i][w] = Maximum value using first i items with capacity w

Transition:

If weight[i-1] ≤ w:

dp[i][w] = max(
    value[i-1] + dp[i-1][w - weight[i-1]],
    dp[i-1][w]
)

Else:

dp[i][w] = dp[i-1][w]

---

## 🎯 Key Learning

- Introduction to Knapsack pattern
- Understanding overlapping subproblems
- Converting recursion → memoization → tabulation
- Backward iteration in space optimization

---

## 🔥 Why This Is Important?

Knapsack pattern is the foundation of:

- Subset Sum
- Equal Partition
- Target Sum
- Count Subsets
- Minimum Subset Difference

Mastering this pattern unlocks a full family of DP problems.

---

## 🏁 Example

weights = [1, 3, 4, 5]  
values  = [1, 4, 5, 7]  
W = 7  

Output: 9