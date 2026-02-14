from collections import defaultdict

def kosaraju_scc(n, edges):
    """
    Find Strongly Connected Components using Kosaraju's Algorithm.
    
    Args:
        n: number of nodes (0 to n-1)
        edges: list of directed edges [u, v]
    
    Returns:
        List of SCCs (each SCC is a list of nodes)
    """
    
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    # Build graph and reverse graph
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    visited = set()
    stack = []
    
    # Step 1: DFS to fill stack by finish time
    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
        stack.append(node)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
    
    # Step 2: DFS on reversed graph
    visited.clear()
    scc_list = []
    
    def reverse_dfs(node, component):
        visited.add(node)
        component.append(node)
        for nei in reverse_graph[node]:
            if nei not in visited:
                reverse_dfs(nei, component)
    
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            reverse_dfs(node, component)
            scc_list.append(component)
    
    return scc_list


# Example Usage
if __name__ == "__main__":
    n = 5
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (1, 3),
        (3, 4)
    ]
    
    result = kosaraju_scc(n, edges)
    print("Strongly Connected Components:", result)
