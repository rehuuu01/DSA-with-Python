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


