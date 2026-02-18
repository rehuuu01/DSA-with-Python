class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path Compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by Rank
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def kruskal_mst(n, edges):
    """
    Kruskal's Algorithm for MST

    Args:
        n: number of vertices (0 to n-1)
        edges: list of edges (u, v, weight)

    Returns:
        total weight of MST
        list of edges in MST
    """

    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(n)
    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges:
        if ds.union(u, v):  # Add edge if no cycle
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges


# Example Usage
if __name__ == "__main__":
    n = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    weight, mst = kruskal_mst(n, edges)
    print("Total MST Weight:", weight)
    print("Edges in MST:", mst)
