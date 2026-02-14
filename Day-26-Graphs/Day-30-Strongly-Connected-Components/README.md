# Day 30 – Strongly Connected Components (Kosaraju’s Algorithm)

## 📌 Topic
Strongly Connected Components (SCC) in Directed Graph

An SCC is a group of vertices in a directed graph such that every vertex is reachable from every other vertex in that group.

---

## 🧠 Problem

Given a directed graph with `n` nodes and a list of edges,  
find all Strongly Connected Components.

---

## ⚙️ Algorithm Used – Kosaraju’s Algorithm

Kosaraju’s Algorithm uses two DFS passes:

### Step 1:
Perform DFS and push nodes into a stack based on finishing time.

### Step 2:
Reverse (transpose) the graph.

### Step 3:
Perform DFS in the order of the stack on the reversed graph.

Each DFS traversal in step 3 gives one SCC.

---

## ⏱ Time & Space Complexity

- Time Complexity: **O(V + E)**
- Space Complexity: **O(V)**

Where:
- V = number of vertices
- E = number of edges

---

## 🧩 Key Concepts Learned

- Finishing time in DFS
- Graph Transpose
- Multi-pass DFS strategy
- Difference between Connected Components and SCC
- Directed graph traversal logic

---

## 🧪 Example

Input:
n = 5
edges = [
(0, 1),
(1, 2),
(2, 0),
(1, 3),
(3, 4)
]


Output:
[[0, 2, 1], [3], [4]]

Explanation:
- {0,1,2} form one SCC
- {3} is alone
- {4} is alone

---

## 📁 Files

- `kosaraju_scc.py` → Implementation
- `tests.txt` → Custom test cases
- `notes.txt` → Intuition & dry run notes

---

## 🚀 Progress

This marks advanced graph territory after:
- BFS & DFS
- Connected Components
- Cycle Detection
- Topological Sort

Strong foundation built for:
- Tarjan’s Algorithm
- Advanced graph interview questions
