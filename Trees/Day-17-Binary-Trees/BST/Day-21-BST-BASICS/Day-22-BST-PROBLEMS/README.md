📘 README.md — Day 22: Binary Search Tree (BST)
📌 Topics Covered

 1. Validate Binary Search Tree

 2. Lowest Common Ancestor (LCA) in BST

 3. Delete a Node in BST

1️⃣ Validate Binary Search Tree

>>Approach 1: Inorder Traversal

Inorder traversal of a valid BST gives strictly increasing values

Track the previously visited node and compare

>>Approach 2: Min–Max Range Method

Each node must lie within a valid (min, max) range

Recursively update constraints for left and right subtrees

Time Complexity: O(n)
Space Complexity: O(h)

2️⃣ Lowest Common Ancestor (LCA) in BST

Idea

If both nodes are smaller → go left

If both nodes are larger → go right

Otherwise → current node is the LCA

Time Complexity: O(h)
Space Complexity: O(1) (iterative)

3️⃣ Delete a Node in BST

Three cases

>>Node is a leaf → delete directly

>>Node has one child → replace node with child

>>Node has two children → replace with inorder successor (minimum in right subtree)

Time Complexity: O(h)
Space Complexity: O(h) (recursive stack)

🧠 Key Learnings

BST properties help reduce unnecessary traversal

Inorder traversal is a powerful validation tool

Delete operation tests complete BST understanding


# Day 23 – Revision (Binary Search Tree)

## Topic Revised
**Delete Node in a Binary Search Tree (BST)**

This revision focuses on optimizing the BST deletion logic by converting the recursive approach into an **iterative solution** to improve space complexity.

---

## Problem: Delete Node in BST

Given the root of a BST and a key, delete the node with the given key while maintaining BST properties.

---

## Approach (Iterative – Optimized)

### Steps:
1. Traverse the BST to find the node to delete and keep track of its parent.
2. Handle three cases:
   - **Leaf node** → remove directly.
   - **Node with one child** → connect parent to the child.
   - **Node with two children**:
     - Find the inorder successor (minimum in right subtree).
     - Replace current node’s value with successor’s value.
     - Delete the successor node.
3. Return the updated root.

---

## Complexity Analysis
- **Time Complexity:** `O(h)`  
- **Space Complexity:** `O(1)` (no recursion stack)

---

## Why Iterative?
- Avoids recursion overhead
- Constant auxiliary space
- More interview-friendly and scalable

---

## Key Learnings
- Time complexity cannot be improved beyond `O(h)` in a BST.
- Space optimization is possible by switching from recursion to iteration.
- Inorder successor is used to safely delete a node with two children.

---

✅ Day 23 was dedicated to strengthening clarity and optimizing existing solutions rather than adding new problems.
