# Day 18 – Binary Trees (BFS & Core Properties)

## Topics Covered
1. Level Order Traversal (Breadth First Search)
2. Height of Binary Tree
3. Count Total Nodes
4. Count Leaf Nodes

---

## 1. Level Order Traversal (BFS)
- Traverses the tree level by level.
- Implemented using a queue.

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

## 2. Height of Binary Tree
- Height is defined as the number of edges in the longest path from root to a leaf.
- Solved using recursion.

**Time Complexity:** O(N)  
**Space Complexity:** O(H), where H is the height of the tree.

---

## 3. Count Total Nodes
- Counts the current node + nodes in left and right subtrees.

**Time Complexity:** O(N)  
**Space Complexity:** O(H)

---

## 4. Count Leaf Nodes
- A leaf node has no left or right child.
- Recursively counts only leaf nodes.

**Time Complexity:** O(N)  
**Space Complexity:** O(H)

---

## Key Learnings
- Most binary tree problems follow the same recursion pattern:
  - Base case (root is None)
  - Solve left subtree
  - Solve right subtree
  - Combine results
- BFS is best handled using a queue, while DFS-based problems are naturally recursive.

---

## Status
✅ Day 18 Completed Successfully
