def dfs_traversal(graph, start):
    """
    DFS traversal of a graph (recursive)
    graph: adjacency list (dict or list of lists)
    start: starting node
    """
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        result.append(node)

        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result


# Example usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print(dfs_traversal(graph, 0))
# Output: [0, 1, 3, 4, 2] (order may vary based on neighbor order)