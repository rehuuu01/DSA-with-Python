import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    """
    Dijkstra's Algorithm for shortest path in weighted graph.
    
    Args:
        n: number of nodes (0 to n-1)
        edges: list of edges (u, v, w)
        source: starting node
        
    Returns:
        List of shortest distances from source
    """
    
    # Step 1: Build adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Remove this line if graph is directed
    
    # Step 2: Initialize distance array
    dist = [float('inf')] * n
    dist[source] = 0
    
    # Step 3: Min heap (distance, node)
    min_heap = [(0, source)]
    
    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)
        
        # Skip outdated entries
        if curr_dist > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
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

source = 0
print(dijkstra(n, edges, source))
