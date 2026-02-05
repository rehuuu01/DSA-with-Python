📅 **DSA Progress:** Day 17 Completed ✔️  
🚀 Next: Level Order Traversal (BFS) & Tree Depth

# Binary Tree Traversals (Preorder, Inorder, Postorder)

This section covers the three fundamental **Depth First Search (DFS)** traversals of a Binary Tree using **recursion**.  
Each traversal is implemented in a **separate Python file** with **user input support** (level-order input).

---

## 🧠 Traversal Types Covered

### 1️⃣ Preorder Traversal (Root → Left → Right)
- Visits the root node first
- Then traverses the left subtree
- Finally traverses the right subtree

📄 File: `preorder_traversal.py`

---

### 2️⃣ Inorder Traversal (Left → Root → Right)
- Traverses the left subtree first
- Visits the root node
- Then traverses the right subtree

📄 File: `inorder_traversal.py`

---

### 3️⃣ Postorder Traversal (Left → Right → Root)
- Traverses the left subtree
- Then traverses the right subtree
- Visits the root node at the end

📄 File: `postorder_traversal.py`

---

## 🔢 Input Format
- Tree nodes are provided in **level order**
- Use `-1` to represent `NULL`

### Example Input
1 2 3 -1 -1 4 5

---

## 📤 Output Example
Preorder : [1, 2, 3, 4, 5]
Inorder : [2, 1, 4, 3, 5]
Postorder : [2, 4, 5, 3, 1]

---

## ⚙️ Implementation Details
- Binary Tree constructed using a **queue (BFS approach)**
- Traversals implemented using **recursive DFS**
- Clean separation of:
  - Tree construction logic
  - Traversal logic
  - Driver code

---

## ⏱ Time & Space Complexity
- **Time Complexity:** `O(N)` for each traversal
- **Space Complexity:** `O(H)` due to recursion stack  
  (`H` = height of the tree)

---

## 📁 Folder Structure
Day-17-Binary-Trees/
├── preorder_traversal.py
├── inorder_traversal.py
└── postorder_traversal.py

---

✅ This implementation follows standard interview and competitive programming practices.
