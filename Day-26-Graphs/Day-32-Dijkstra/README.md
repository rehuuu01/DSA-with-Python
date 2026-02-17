# Day 32 – Dijkstra’s Algorithm (Shortest Path in Weighted Graph)

## 📌 Topic
Dijkstra’s Algorithm – Shortest Path in Weighted Graph (Non-Negative Weights)

---

## 🧠 Problem Statement

Given:
- A weighted graph
- A source node

Find the shortest distance from the source node to all other nodes.

⚠️ Condition: All edge weights must be non-negative.

---

## 🚀 Why Not BFS?

- BFS works only for unweighted graphs (or equal weights).
- In weighted graphs, we must always expand the node with the minimum distance.
- That’s why we use a **Min Heap (Priority Queue)**.

---

## ⚙️ Algorithm Steps

1. Initialize a distance array with infinity.
2. Set `distance[source] = 0`.
3. Use a Min Heap to always process the node with the smallest distance.
4. For every adjacent node:
   - Relax the edge.
   - Update distance if a shorter path is found.
5. Repeat until heap is empty.

---

## 🏗️ Graph Representation

We use an adjacency list:

graph[u] = [(v, weight), (v2, weight2), ...]

---

## 🧑‍💻 Implementation (Python)

```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    graph = defaultdict(list)
    
    # Build graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Remove for directed graph
    
    dist = [float('inf')] * n
    dist[source] = 0
    
    min_heap = [(0, source)]
    
    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)
        
        if curr_dist > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))
    
    return dist


# Example Usage
n = 5
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]

print(dijkstra(n, edges, 0))

⏱️ Complexity Analysis

Time Complexity: O((V + E) log V)
Space Complexity: O(V)

🧩 Edge Cases

- Single node graph
- Disconnected graph
- Graph with large weights
- Source node isolated

🔥 Key Learning

Difference between BFS and Dijkstra

Concept of edge relaxation

Why outdated heap entries must be skipped

Why Dijkstra fails with negative weights

📌 Folder Structure

Day-32-Dijkstra/
├── dijkstra.py
├── README.md
└── notes.txt