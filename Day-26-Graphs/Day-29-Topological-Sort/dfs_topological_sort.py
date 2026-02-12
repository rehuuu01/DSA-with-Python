from collections import defaultdict

def topological_sort_dfs(n, edges):
    """
    Topological Sort using DFS
    """
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * n
    stack = []
    
    def dfs(node):
        visited[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]


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

result = topological_sort_dfs(n, edges)
print("Topological Order (DFS):", result)
