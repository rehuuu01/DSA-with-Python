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
