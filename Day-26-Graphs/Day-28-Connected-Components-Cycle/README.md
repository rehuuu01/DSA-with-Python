# Day 28 – Graph Applications (DFS)

## Topics Covered
1. Connected Components in an Undirected Graph  
2. Cycle Detection in an Undirected Graph  

These problems apply basic **DFS traversal** to solve real graph use-cases.

---

## 1️⃣ Connected Components

### Problem
Given an undirected graph with `n` nodes, count how many connected components exist.

### Approach
- Build an adjacency list
- Use DFS to traverse the graph
- Each time DFS starts from an unvisited node, it represents a new component

### Key Insight
> Number of DFS calls = number of connected components

### Time & Space Complexity
- **Time:** O(n + e)
- **Space:** O(n + e)

---

## 2️⃣ Cycle Detection in Undirected Graph

### Problem
Determine whether an undirected graph contains a cycle.

### Approach
- Use DFS with **parent tracking**
- If a visited node is encountered that is **not the parent**, a cycle exists

### Key Insight
> In undirected graphs, revisiting a non-parent node implies a cycle

### Time & Space Complexity
- **Time:** O(n + e)
- **Space:** O(n + e)

---

## Learnings from Day 28
- DFS is not just traversal, it’s a problem-solving tool
- Parent tracking is crucial for cycle detection
- Graph problems often reduce to “how many times DFS/BFS is started”

---

📌 **Next Topics**
- Bipartite Graph
- Directed Graph Cycle Detection
- Topological Sort
