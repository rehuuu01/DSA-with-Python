## Day 9 – Hashing Basics (Arrays)

### Problems Solved
1. Two Sum
2. Frequency of Elements in an Array
3. Element Appearing Once (Others Appear Twice)
4. Count occurrences of an element
5. - Longest Subarray with Sum K

### Key Concepts Learned
- Hashing using Python dictionary
- Complement-based problem solving
- Frequency counting technique
- Difference between sequential and nested loops
- Why two loops do NOT always mean O(n²)
-  Frequency counting / Linear traversal
- Hashmaps help avoid nested loops

### Time & Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

### Key Takeaways
- Hashing helps reduce brute force solutions
- Count first, then decide (important for frequency problems)
- Clean logic is more important than clever tricks initially


## 📅 Day 10 – Hashing & Prefix Sum

### ✅ Problems Solved

1. **Majority Element (More than N/2 times)**
2. **Count Subarrays with Sum = K**

---

### 🧠 Problem 1: Majority Element (More than N/2 times)

**Problem Statement:**  
Given an array of size `N`, find the element that appears **more than N/2 times**, if it exists.

**Approaches Explored:**
- Brute Force – O(n²)
- Sorting Method – O(n log n)
- Hashing – O(n) time, O(n) space
- **Moore’s Voting Algorithm – O(n) time, O(1) space (Optimal)**

**Key Learnings:**
- There can be **at most one majority element** in an array.
- Hashing helps reduce time complexity by storing frequencies.
- Moore’s Voting Algorithm works by **canceling out different elements**, leaving the majority as the final candidate.
- Moore’s Voting is the **most optimized solution** due to constant space usage.
- Important interview insight: Moore’s algorithm gives a *candidate*, which may require verification if the majority is not guaranteed.

---

### 🧠 Problem 2: Count Subarrays with Sum = K

**Problem Statement:**  
Given an array and an integer `K`, count the total number of **continuous subarrays** whose sum equals `K`.

**Key Concepts Used:**
- Prefix Sum
- Hash Map (Frequency Count)

**Key Learnings:**
- Brute force checking of all subarrays leads to O(n²) time and is inefficient.
- Prefix sums help convert the subarray sum problem into a difference problem.
- For every index, if `(current_prefix_sum - K)` has appeared before, it contributes to valid subarrays.
- A frequency map (not index map) is required because **multiple subarrays can end at the same index**.
- Initializing prefix sum frequency with `{0: 1}` is crucial to handle subarrays starting from index `0`.
- This pattern is reusable in many advanced subarray problems.

---

### ⏱️ Overall Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) (O(1) for Moore’s Voting Algorithm)

---

### 🚀 Key Takeaway from Day 10
> Hashing and prefix sums allow us to trade space for time and reduce complex subarray problems to linear-time solutions.

---
