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

