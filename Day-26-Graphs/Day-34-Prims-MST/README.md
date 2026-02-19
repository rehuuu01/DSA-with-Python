# Day 34 – Prim’s Algorithm (Minimum Spanning Tree)

## 📌 Problem
Find the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph using Prim’s Algorithm.

---

## 🌳 What is Prim’s Algorithm?

Prim’s Algorithm is a greedy algorithm that builds the Minimum Spanning Tree (MST) by:

1. Starting from any node.
2. Always picking the smallest edge that connects a visited node to an unvisited node.
3. Repeating until all nodes are included.

---

## 🧠 Key Concepts

- Greedy Algorithm
- Min Heap (Priority Queue)
- Undirected Weighted Graph
- Difference between MST and Shortest Path

⚠ Prim’s ≠ Dijkstra  
Prim → Builds MST  
Dijkstra → Finds shortest path from source

---

## ⏱ Time Complexity

O(E log V)

Where:
- V = number of vertices
- E = number of edges

---

## 📦 Space Complexity

O(V)

---

## ✅ Implementation Highlights

- Used `heapq` for priority queue
- Maintained a visited set
- Avoided cycles by checking visited nodes
- Calculated total MST weight

---

## 📂 Folder Structure
Day-34-Prims-MST/
│
├── prims.py
├── notes.txt
└── README.md


---

## 🚀 Learning Outcome

- Understood how greedy works in MST
- Learned difference between Prim’s and Kruskal
- Strengthened heap concepts in graphs
