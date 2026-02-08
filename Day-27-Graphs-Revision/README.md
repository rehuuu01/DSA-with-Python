# Day 27 – Revision (Graphs)

## Topic Revised
**Graph Traversal – BFS & DFS**

This day is dedicated to revisiting and strengthening the core concepts of **Breadth First Search (BFS)** and **Depth First Search (DFS)** to ensure deep understanding before moving to advanced graph problems.

---

## Concepts Covered

### 1. Breadth First Search (BFS)
- Uses **Queue**
- Traverses graph **level by level**
- Best suited for:
  - Shortest path in unweighted graphs
  - Level-order traversal
- Important detail:
  - Mark node as visited **before** pushing into queue to avoid duplicates

**Time Complexity:** `O(V + E)`  
**Space Complexity:** `O(V)`

---

### 2. Depth First Search (DFS)
- Uses **Recursion / Stack**
- Traverses graph **depth-wise**
- Best suited for:
  - Connected components
  - Cycle detection
  - Topological logic (later)

**Time Complexity:** `O(V + E)`  
**Space Complexity:** `O(V)` (recursion stack)

---

## Key Learnings from Revision
- Clear difference between BFS and DFS traversal patterns
- Importance of `visited` array/set placement
- How traversal behaves in disconnected graphs
- Built intuition instead of memorizing code

---

## Why This Revision Matters
Graph traversal is the foundation for:
- Connected Components
- Cycle Detection
- Bipartite Graphs
- Shortest Paths
- Topological Sorting

Revisiting these basics ensures fewer bugs and stronger confidence in upcoming graph problems.

---

## Status
✅ Concepts Revised  
✅ Code Reviewed & Understood  
✅ Ready to move forward with Graph Applications 🚀
