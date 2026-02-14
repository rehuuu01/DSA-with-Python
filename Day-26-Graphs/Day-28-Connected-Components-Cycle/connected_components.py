def count_components(n, edges):
    """
    Count number of connected components in an undirected graph.

    Args:
        n (int): number of nodes (0 to n-1)
        edges (List[List[int]]): list of undirected edges

    Returns:
        int: number of connected components
    """
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            dfs(node)
            components += 1

    return components


# ---------- Example Usage ----------
n = 5
edges = [[0, 1], [1, 2], [3, 4]]

print("Connected Components:", count_components(n, edges))
# Output: 2
