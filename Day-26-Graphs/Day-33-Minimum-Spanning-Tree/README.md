# Day 33 – Minimum Spanning Tree (Kruskal’s Algorithm)

## 📌 Topic Covered
- Spanning Tree
- Minimum Spanning Tree (MST)
- Greedy Algorithm
- Disjoint Set (Union-Find)
- Path Compression
- Union by Rank

---

## 🌳 What is a Spanning Tree?

A spanning tree of a connected, undirected graph:
- Connects all vertices
- Has exactly (V - 1) edges
- Contains no cycles

---

## 🌳 What is Minimum Spanning Tree?

The spanning tree with minimum total edge weight.

---

## ⚡ Kruskal’s Algorithm

### Approach:
1. Sort all edges in increasing order of weight.
2. Use Disjoint Set to detect cycles.
3. Add edge if it does not form a cycle.
4. Stop when (V - 1) edges are included.

---

## 🧠 Key Concepts Used

### Disjoint Set (Union-Find)
- Path Compression
- Union by Rank
- Efficient cycle detection

---

## ⏱️ Time Complexity

O(E log E)

- Sorting edges → O(E log E)
- Union-Find operations → Nearly O(1)

---

## 📂 Files in This Folder

- kruskal_mst.py
- notes.txt
- README.md

---

## 🚀 Learning Outcome

Today I learned:
- How to build Minimum Spanning Tree
- How greedy strategy works in graphs
- Advanced usage of Disjoint Set
- Efficient cycle detection in undirected graphs
