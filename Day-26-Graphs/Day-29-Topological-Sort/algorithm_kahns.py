from collections import deque, defaultdict

def topological_sort_kahn(n, edges):
    """
    Topological Sort using Kahn's Algorithm (BFS)
    
    Args:
        n: number of nodes (0 to n-1)
        edges: list of directed edges [u, v]
    
    Returns:
        Topological order list (if DAG)
        Empty list if cycle exists
    """
    
    # Step 1: Build graph
    graph = defaultdict(list)
    indegree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    # Step 2: Push nodes with indegree 0
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    
    topo_order = []
    
    # Step 3: BFS
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check cycle
    if len(topo_order) == n:
        return topo_order
    else:
        return []  # Cycle exists


# ---------------- Example Usage ----------------
n = 6
edges = [
    [5, 2],
    [5, 0],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]

result = topological_sort_kahn(n, edges)
print("Topological Order (Kahn):", result)
