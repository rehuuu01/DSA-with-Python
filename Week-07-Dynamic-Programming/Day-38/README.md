# Day 38 – Dynamic Programming Revision

## 🎯 Goal of the Day
Strengthen Dynamic Programming fundamentals by revisiting:
- Fibonacci (all approaches)
- Climbing Stairs
- Core DP Concepts

---

## 🔁 Problems Revised

### 1️⃣ Fibonacci

Approaches Implemented:
- Recursive (Exponential)
- Memoization (Top-Down DP)
- Tabulation (Bottom-Up DP)
- Space Optimized

Time Complexity Comparison:

| Approach        | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| Recursion      | O(2^n)          | O(n) stack       |
| Memoization    | O(n)            | O(n)             |
| Tabulation     | O(n)            | O(n)             |
| Space Optimized| O(n)            | O(1)             |

---

### 2️⃣ Climbing Stairs

Approaches:
- Memoization
- Tabulation
- Space Optimized

Observation:
Climbing Stairs follows the Fibonacci pattern:
dp[n] = dp[n-1] + dp[n-2]

---

## 🧠 Key DP Concepts Revised

- Overlapping Subproblems
- Optimal Substructure
- Memoization vs Tabulation
- How to Identify DP Problems

---

## 💡 Key Learnings

✔ Recursion becomes inefficient due to repeated computations  
✔ Memoization avoids recomputation using caching  
✔ Tabulation builds solution bottom-up  
✔ Space optimization is possible when only previous states are required  
✔ DP problems often follow patterns (Fibonacci type, choice-based, grid-based)

---

## 🚀 Why This Revision Matters

Dynamic Programming is about:
- Pattern recognition
- State definition
- Transition relation

Strong fundamentals make advanced DP much easier.

---

## 📌 Status

Day 38 Completed ✔  
DP Foundation Strengthened 🔥  
Ready to move to 1D DP problems next.