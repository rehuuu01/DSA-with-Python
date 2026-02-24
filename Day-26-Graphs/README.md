# Week 06 – Graphs

## 📌 Overview

This week focused on mastering Graph Data Structures and Algorithms,
covering traversal, cycle detection, shortest paths, minimum spanning trees,
and advanced graph algorithms.

Graphs are one of the most important topics for technical interviews.

---

## 📚 Topics Covered

### 🔹 Graph Basics
- Graph Representation (Adjacency List)
- BFS (Breadth First Search)
- DFS (Depth First Search)

### 🔹 Graph Applications
- Connected Components
- Cycle Detection (Undirected Graph)
- Topological Sort (Kahn’s Algorithm – BFS)

### 🔹 Strongly Connected Components
- Kosaraju’s Algorithm
- Graph Transpose
- Finishing Time Stack Logic

---

## 🚀 Shortest Path Algorithms

### 1️⃣ Shortest Path in Unweighted Graph
- BFS based approach
- Time Complexity: O(V + E)

### 2️⃣ Dijkstra’s Algorithm
- Min Heap (Priority Queue)
- Works for non-negative weights
- Time Complexity: O(E log V)

### 3️⃣ Bellman-Ford Algorithm
- Handles negative weights
- Detects negative weight cycles
- Time Complexity: O(V * E)

### 4️⃣ Floyd–Warshall Algorithm
- All-Pairs Shortest Path
- Dynamic Programming based
- Time Complexity: O(V³)

---

## 🌲 Minimum Spanning Tree (MST)

### 1️⃣ Kruskal’s Algorithm
- Greedy approach
- Uses Disjoint Set (Union-Find)
- Path Compression + Union by Rank
- Time Complexity: O(E log E)

### 2️⃣ Prim’s Algorithm
- Min Heap based
- Greedy expansion
- Time Complexity: O(E log V)

---

## 🧠 Key Concepts Learned

- Graph Representation (Adjacency List)
- BFS & DFS Traversals
- Cycle Detection
- Topological Ordering
- Strongly Connected Components
- Shortest Path Algorithms
- Minimum Spanning Tree
- Greedy vs Dynamic Programming approaches in graphs
- Negative cycle detection

---

## 📂 Folder Structure

Day-26-Graphs/
│
├── Day-26-BFS-DFS/
├── Day-27-Revision/
├── Day-28-Connected-Components-Cycle/
├── Day-29-Topological-Sort/
├── Day-30-Strongly-Connected-Components/
├── Day-31-Shortest-Path-Unweighted/
├── Day-32-Dijkstra/
├── Day-33-Minimum-Spanning-Tree/
├── Day-34-Prims-MST/
├── Day-35-Bellman-ford/
├── Day-36-Floyd-Warshall/
└── README.md

---

## 📌 Summary

Week 06 completed with advanced graph mastery.

From basic traversals to:
- All shortest path variants
- MST algorithms
- SCC detection
- Negative cycle handling

This marks strong progress toward interview-level DSA preparation.