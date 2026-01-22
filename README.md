# DSA with Python 🚀

This repository contains my structured **DSA preparation using Python**
for product-based software engineering roles.

## Structure
- Week-wise topic folders
- Clean Python implementations
- Interview-focused approach

## Topics Covered
- Time & Space Complexity
- Arrays
- Recursion

## Language
- Python

# Day 11 – Sliding Window (Fixed Size)

## 📌 Topics Covered
- Sliding Window Technique (Fixed Size)
- Window expansion and contraction
- Using auxiliary data structures with sliding window

---

## ✅ Problems Solved

### 1️⃣ Maximum Sum Subarray of Size K
**Problem Statement:**  
Given an array of integers and a number `k`, find the maximum sum of any contiguous subarray of size `k`.

**Approach:**  
- Maintain a running window sum of size `k`
- Slide the window by removing the element going out and adding the new element
- Update maximum sum at each step

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### 2️⃣ First Negative Integer in Every Window of Size K
**Problem Statement:**  
Given an array and an integer `k`, find the first negative number in every contiguous subarray of size `k`.  
If a window does not contain a negative number, output `0`.

**Approach:**  
- Use a fixed-size sliding window
- Maintain a queue (deque) to store indices of negative elements
- Remove indices that move out of the window
- The front of the queue always represents the first negative number

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(k)`

---

## 🧠 Key Learnings
- Sliding Window reduces nested loops into a single traversal
- Fixed-size window problems often avoid recomputation
- Deque is essential when tracking window-based elements efficiently
- Always watch for hidden `O(n²)` operations like `pop(0)` in lists

---

## 🚀 Summary
Day 11 focused on mastering the **Fixed Size Sliding Window** pattern — a core interview concept used to optimize brute-force solutions into efficient linear-time algorithms.

Consistency maintained. Ready to move to variable-size windows.

---
## Day 12 – Variable Size Sliding Window

### Problems Solved:
1. Longest Subarray with Sum at Most K
2. Longest Substring Without Repeating Characters
3. Minimum Size Subarray Sum (>= K)

---

### 1. Longest Subarray with Sum at Most K
Approach:
Used a variable-size sliding window. Expanded the window using the right pointer and
shrunk it from the left whenever the sum exceeded K. Tracked the maximum valid window length.

Time Complexity: O(n)  
Space Complexity: O(1)

Note:
This approach works only for non-negative numbers.

---

### 2. Longest Substring Without Repeating Characters
Approach:
Used a sliding window with a hashmap to store the last seen index of each character.
When a duplicate character appeared inside the window, moved the left pointer
to the index after its previous occurrence.

Time Complexity: O(n)  
Space Complexity: O(n)

---

### 3. Minimum Size Subarray Sum (>= K)
Approach:
Expanded the window until the sum reached or exceeded the target.
Then shrunk the window aggressively to find the minimum possible window size.

Time Complexity: O(n)  
Space Complexity: O(1)

---

### Key Learnings:
- Sliding window optimization over brute force
- Window expansion and contraction logic
- Importance of constraints (negative vs non-negative arrays)
- Interview pattern recognition

