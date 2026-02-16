from collections import deque, defaultdict

def shortest_path_unweighted(n, edges, source):
    """
    Finds shortest distance from source to all nodes
    in an unweighted graph using BFS.

    Args:
        n: number of nodes (0 to n-1)
        edges: list of edges [u, v]
        source: starting node

    Returns:
        List of distances
    """

    # Step 1: Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Remove this if graph is directed

    # Step 2: Distance array
    dist = [-1] * n
    dist[source] = 0

    # Step 3: BFS
    queue = deque([source])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


# Example Usage
n = 6
edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 4],
    [4, 5]
]

source = 0

print(shortest_path_unweighted(n, edges, source))
