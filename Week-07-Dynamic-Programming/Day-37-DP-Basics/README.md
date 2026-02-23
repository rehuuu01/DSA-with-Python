# Day 37 - Dynamic Programming (Basics)

## 📌 Topics Covered

- Introduction to Dynamic Programming
- Overlapping Subproblems
- Optimal Substructure
- Memoization (Top-Down)
- Tabulation (Bottom-Up)
- Space Optimization
- Fibonacci Problem
- Climbing Stairs Problem

---

## 🧠 What is Dynamic Programming?

Dynamic Programming (DP) is an optimization technique used to solve
problems that have:

1. Overlapping Subproblems  
2. Optimal Substructure  

Instead of recalculating results, we store them and reuse them.

---

## 🚀 Problems Implemented

### 1️⃣ Fibonacci
Implemented using:
- Recursive approach
- Memoization (Top-Down)
- Tabulation (Bottom-Up)
- Space Optimized approach

Time complexity improved from **O(2^n)** to **O(n)**.

---

### 2️⃣ Climbing Stairs
Problem:
You can climb 1 or 2 steps.
Find number of distinct ways to reach the top.

This follows the Fibonacci pattern:

ways(n) = ways(n-1) + ways(n-2)

Implemented using:
- Recursive
- Memoization
- Tabulation
- Space Optimized approach

---

## 🏆 Key Learnings

- Identifying overlapping subproblems
- Converting recursion into DP
- Reducing exponential time to linear time
- Space optimization techniques
- Recognizing Fibonacci pattern in problems

---

## 📂 Folder Structure
Week-07-Dynamic-Programming/
│
└── Day-37-DP-Basics/
├── fibonacci.py
├── climbing_stairs.py
├── notes.txt
└── README.md

---

## 🎯 Next Step

Move to 2D Dynamic Programming:
- Unique Paths
- Minimum Path Sum

Dynamic Programming journey has officially begun 🚀🔥