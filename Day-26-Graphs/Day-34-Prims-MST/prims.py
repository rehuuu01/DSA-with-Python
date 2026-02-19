import heapq

def prims_algorithm(n, adj):
    """
    Prim's Algorithm using Min Heap
    
    Args:
        n: number of nodes (0 to n-1)
        adj: adjacency list {node: [(neighbor, weight)]}
    
    Returns:
        total weight of MST
    """
    
    visited = set()
    min_heap = [(0, 0)]  # (weight, node)
    total_weight = 0
    
    while min_heap and len(visited) < n:
        weight, node = heapq.heappop(min_heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        total_weight += weight
        
        for neighbor, w in adj[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor))
    
    return total_weight


# Example Usage
if __name__ == "__main__":
    n = 5
    
    adj = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8)],
        4: [(1, 5), (2, 7)]
    }
    
    print("MST Total Weight:", prims_algorithm(n, adj))
