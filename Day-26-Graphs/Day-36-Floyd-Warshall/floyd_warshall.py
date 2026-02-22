def floyd_warshall(n, edges):
    """
    Floyd-Warshall Algorithm
    Finds shortest distances between all pairs of vertices
    
    Args:
        n: number of vertices (0 to n-1)
        edges: list of edges (u, v, weight)
        
    Returns:
        distance matrix
    """
    
    # Step 1: Initialize distance matrix
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    # Distance to self = 0
    for i in range(n):
        dist[i][i] = 0
    
    # Step 2: Fill direct edges
    for u, v, w in edges:
        dist[u][v] = w
    
    # Step 3: Dynamic Programming
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


# ✅ Example Usage
if __name__ == "__main__":
    n = 4
    edges = [
        (0, 1, 3),
        (0, 3, 7),
        (1, 2, 1),
        (2, 3, 2)
    ]
    
    result = floyd_warshall(n, edges)
    
    print("All-Pairs Shortest Path Matrix:")
    for row in result:
        print(row)