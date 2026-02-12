# Day 29 – Graph Applications (Topological Sort)

## Topic Covered
Topological Sort in Directed Acyclic Graph (DAG)

Topological sorting is a linear ordering of vertices such that for every directed edge u → v, node u appears before v in the ordering.

Important: Topological Sort only works for Directed Acyclic Graphs (DAG).

---

## Methods Implemented

### 1️⃣ Kahn’s Algorithm (BFS + Indegree)

Approach:
1. Calculate indegree of all vertices
2. Push all nodes with indegree = 0 into a queue
3. Process queue using BFS
4. Reduce indegree of neighbors
5. If all nodes are processed → DAG
   Else → Cycle exists

Time Complexity: O(V + E)
Space Complexity: O(V)

---

### 2️⃣ DFS Based Topological Sort

Approach:
1. Perform DFS traversal
2. Push node to stack after visiting all neighbors
3. Reverse stack to get topological order

Time Complexity: O(V + E)
Space Complexity: O(V)

---

## Key Learnings

- Understanding indegree concept
- Why Topological Sort works only in DAG
- Cycle detection using Kahn’s Algorithm
- Difference between BFS and DFS approaches
- Real-world use cases like course scheduling and dependency resolution

---

## Interview Problems Related

- Course Schedule I
- Course Schedule II
- Alien Dictionary
- Detect Cycle in Directed Graph

---

Day 29 strengthens graph application concepts and prepares for advanced dependency-based problems.
