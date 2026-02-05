# Day 20 – Binary Tree Properties 🌳

This day focuses on important **Binary Tree properties** that are frequently asked in interviews.  
The goal was to strengthen recursion intuition and optimize DFS-based solutions.

---

## ✅ Topics Covered

### 1️⃣ Maximum Depth of Binary Tree
- Used recursive DFS
- Depth of a node = `1 + max(left_depth, right_depth)`
- Helps build foundation for advanced tree problems

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

### 2️⃣ Diameter of Binary Tree
- Diameter = longest path between any two nodes (in edges)
- For each node: `left_height + right_height`
- Height calculated using postorder traversal
- Optimized to compute height and diameter in one traversal

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

### 3️⃣ Check if Binary Tree is Height Balanced
- Tree is balanced if height difference ≤ 1 for every node
- Used optimized recursion:
  - Return height if balanced
  - Return `-1` immediately if unbalanced
- Avoids repeated height calculations

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

## 🧠 Key Learnings
- Postorder DFS is crucial for tree property problems
- Returning values from recursion can optimize performance
- Same recursion template can solve multiple problems

---

📌 These problems build a strong base for advanced Binary Tree and BST questions.
