# Week 02 – Arrays

## 📘 Concepts Covered
- Introduction to Arrays
- Array traversal
- Linear Time Complexity (O(n))
- In-place operations
- Handling edge cases

## 🧠 Problems Solved
1. Find maximum element in an array  
   - Time Complexity: O(n)  
   - Space Complexity: O(1)
   - Key Learning: Linear traversal / Variable tracking


2. Find second largest element in an array  
   - Time Complexity: O(n)  
   - Space Complexity: O(1)
   - Key Learning: Linear traversal / Edge case handling


3. Reverse an array using two pointers  
   - Time Complexity: O(n)  
   - Space Complexity: O(1)
   - Key Learning: Two pointer technique / In-place modification

   
## Day 4 – Arrays (Basic Operations)

### Problems Solved:
1. Check if array is sorted 
- Key Learning: Adjacent comparison / Early termination
2. Linear search
- Key Learning: Linear traversal / Early exit condition
3. Count occurrences of an element
- Key Learning: Frequency counting / Linear traversal

### Concepts Practiced:
- Array traversal
- Comparison logic
- Counters
- Time complexity O(n)

## 💻 Language Used
- Python

## 📌 Key Learnings
- How to traverse arrays efficiently
- How to solve problems without sorting
- Using constant extra space
- Writing clean and interview-ready code

### Day 5 – Array Patterns
Solved:
1. Remove duplicates from array 
- Key Learning: Two pointer technique / In-place unique filtering
2. Left rotate array by one
- Key Learning: Index shifting / In-place rotation


Concepts:
- Two-pointer technique
- In-place array manipulation
- Array rotation logic

### Day 6 – Array Manipulation (Two Pointer Technique)

Solved:
1. Move All Zeros to End
- Key Learning: Two pointer technique / Stable in-place rearrangement

Revised / Reinforced:
- Second Largest Element in Array
- Check if Array is Sorted
- Reverse Array (In-place)

Key Concepts:
- Two-pointer technique
- In-place array modification
- Edge case handling

Time & Space Complexity:
- Time: O(n)
- Space: O(1)

Notes:
Reinforced previously learned array problems and focused on debugging and optimization.
 
 ### Day 7 – Arrays (Hashing & Rotation)
✅ Problems Solved

 1. Left Rotate Array by K Positions
 2. Union of Two Arrays
 3. Intersection of Two Arrays

 1. Left Rotate Array by K Positions
  - Problem Statement
Given an array of size n and an integer k, rotate the array to the left by k positions.
# Key Learnings
- Understanding array rotation mechanics
- Handling cases where k > n using k = k % n
- Difference between:
- Brute force shifting
- Optimized in-place approach
- Index manipulation without extra space
- Common interview question on arrays

⏱️ Time & Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

2.  Union of Two Arrays (Using Hashing)
 -  Problem Statement
Given two arrays, find the union containing all unique elements from both arrays.
🧠 Key Learnings
- Use of hashing via Python set
- Sets automatically eliminate duplicates
- Explicit loops improve conceptual clarity
- When to prefer hashing over nested loops
- Real-world use of hash tables in arrays

⏱️ Time & Space Complexity
- Time Complexity: O(n + m)
- Space Complexity: O(n + m)

3. Intersection of Two Arrays (Using Hashing)
- Problem Statement
Given two arrays, find the elements that are common in both arrays.
🧠 Key Learnings
- Converting an array into a hash set for O(1) lookup
- Efficient membership checking using hashing
- Avoiding duplicates in the result
- Core interview concept: Hashing + Arrays

⏱️ Time & Space Complexity
- Time Complexity: O(n + m)
- Space Complexity: O(m)

## Day 8 – Arrays (Prefix Sum & Hashing)

### Problems Solved:
- Find Missing Number
- Longest Subarray with Sum K

### Key Learnings:
- Prefix sum stores cumulative information
- Hashmaps help avoid nested loops
- Reduced O(n²) solutions to O(n)

## Day 9 – Hashing Basics (Arrays)

### Problems Solved
1. Two Sum
2. Frequency of Elements in an Array
3. Element Appearing Once (Others Appear Twice)

### Key Concepts Learned
- Hashing using Python dictionary
- Complement-based problem solving
- Frequency counting technique
- Difference between sequential and nested loops
- Why two loops do NOT always mean O(n²)

### Time & Space Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

### Key Takeaways
- Hashing helps reduce brute force solutions
- Count first, then decide (important for frequency problems)
- Clean logic is more important than clever tricks initially
