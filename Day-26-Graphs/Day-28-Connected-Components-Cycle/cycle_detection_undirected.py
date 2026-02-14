def has_cycle(n, edges):
    """
    Detect cycle in an undirected graph using DFS.

    Args:
        n (int): number of nodes (0 to n-1)
        edges (List[List[int]]): list of undirected edges

    Returns:
        bool: True if cycle exists, else False
    """
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


# ---------- Example Usage ----------
n = 3
edges = [[0, 1], [1, 2], [2, 0]]

print("Cycle Exists:", has_cycle(n, edges))
# Output: True
