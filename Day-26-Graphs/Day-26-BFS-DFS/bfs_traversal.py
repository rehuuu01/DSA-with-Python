from collections import deque

def bfs_traversal(graph, start):
    """
    BFS traversal of a graph
    graph: adjacency list (dict or list of lists)
    start: starting node
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

print(bfs_traversal(graph, 0))  # Output: [0, 1, 2, 3, 4]