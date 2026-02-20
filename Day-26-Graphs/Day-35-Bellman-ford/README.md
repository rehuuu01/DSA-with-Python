def bellman_ford(n, edges, source):
    """
    Bellman-Ford Algorithm
    Finds shortest path from source to all vertices.
    Detects negative weight cycle.

    Args:
        n: number of vertices (0 to n-1)
        edges: list of (u, v, weight)
        source: starting vertex

    Returns:
        distance list if no negative cycle
        None if negative cycle exists
    """

    # Step 1: Initialize distances
    dist = [float('inf')] * n
    dist[source] = 0

    # Step 2: Relax edges (n-1) times
    for _ in range(n - 1):
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    # Step 3: Check for negative weight cycle
    for u, v, wt in edges:
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            print("Negative weight cycle detected!")
            return None

    return dist


# Example Usage
n = 5
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

source = 0

result = bellman_ford(n, edges, source)

if result:
    print("Shortest distances from source:", result)