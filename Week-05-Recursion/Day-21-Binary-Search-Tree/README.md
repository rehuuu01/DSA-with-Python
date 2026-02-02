# Day 21: Binary Search Tree (BST)

## 📌 Overview
On Day 21, we covered the fundamentals of **Binary Search Trees (BST)**.  
BST is a special type of Binary Tree that allows efficient searching, insertion, and retrieval of values using ordering properties.

---

## 🌳 What is a Binary Search Tree?
A Binary Search Tree follows this rule for every node:

- Left subtree contains values **less than** the node
- Right subtree contains values **greater than** the node

This property enables optimized operations compared to a normal Binary Tree.

---

## 📚 Topics Covered

### 1️⃣ Search in a BST
- Implemented using an **iterative approach**
- Uses BST property to skip unnecessary nodes

### 2️⃣ Insert into a BST
- Inserted values while maintaining BST property
- New nodes are always added at a **leaf position**

### 3️⃣ Inorder Traversal
- Traversal order: **Left → Root → Right**
- In a BST, inorder traversal always returns values in **sorted order**

### 4️⃣ Minimum & Maximum in BST
- Minimum value → **leftmost node**
- Maximum value → **rightmost node**
- Implemented iteratively for optimal space usage

---

## 📂 Folder Structure
Day-21-Binary-Search-Tree/
│── search_in_bst.py
│── insert_into_bst.py
│── inorder_traversal.py
│── min_max_in_bst.py
│── README.md

---

## ⏱️ Time & Space Complexity

| Operation | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Search | O(h) | O(1) |
| Insert | O(h) | O(1) |
| Inorder Traversal | O(n) | O(h) |
| Min / Max | O(h) | O(1) |

> `h` = height of the BST  
> `n` = number of nodes

---

## 🎯 Key Learnings
- BST provides faster operations compared to normal Binary Trees
- Inorder traversal is a powerful tool to verify BST correctness
- Iterative solutions help avoid recursion stack overhead
- Understanding BST properties simplifies many tree problems

---

## ✅ Status
**Day 21 completed successfully** 🚀  
Next topic: **Validate BST and Delete Node in BST**
