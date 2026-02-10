# Day 26 – Graph Basics (BFS & DFS)

## 📌 Topic
**Graph Traversal using Breadth First Search (BFS) and Depth First Search (DFS)**

Graphs are used to represent relationships between entities and are commonly asked in product-based company interviews.

---

## 📘 Graph Representation
The graph is represented using an **Adjacency List**, where:
- Each node stores a list of its neighboring nodes
- This representation is space-efficient and widely used

Example:
```python
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

🔹 Breadth First Search (BFS)
Approach
 - Uses a queue
- Traverses the graph level by level
- Maintains a visited set to avoid revisiting nodes

##Steps
1. Start from the given node

2. Mark it as visited and push into queue

3. Pop from queue, visit neighbors

4. Push unvisited neighbors into queue

##Time & Space Complexity

. Time: O(V + E)
. Space: O(V)

🔹 Depth First Search (DFS)
Approach

. Uses recursion (implicit stack)
. Traverses the graph by going deep first
. Maintains a visited set

##Steps
1. Start from the given node
2. Mark node as visited
3. Recursively visit all unvisited neighbors

##Time & Space Complexity

. Time: O(V + E)
. Space: O(V) (recursion stack + visited)

🧠 Key Interview Notes 

. BFS uses a queue, DFS uses recursion or stack
. visited array/set is mandatory to avoid infinite loops
.  Traversal order may vary based on adjacency list
. DFS order is not unique

📂 Files Included
|-bfs_traversal.py
|-dfs_traversal.py
|-README.md

✅ Status
Graph traversal fundamentals completed successfully 🚀
** Ready to move to Connected Components / Number of Provinces

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
