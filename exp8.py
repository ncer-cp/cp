import sys

# Number of vertices in the graph
V = 5

# Function to find the vertex with the minimum key value
def minKey(key, mstSet):
    min_val = sys.maxsize
    min_index = -1
    for v in range(V):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

# Function to print MST stored in parent[]
def printMST(parent, graph):
    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Function to construct MST using Prim's algorithm
def primMST(graph):
    key = [sys.maxsize] * V     # Initialize all keys as INFINITE
    parent = [None] * V         # To store constructed MST
    key[0] = 0                  # First vertex key is 0
    mstSet = [False] * V        # To represent the MST set

    parent[0] = -1  # First node is always the root of MST

    for _ in range(V):
        u = minKey(key, mstSet)
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    printMST(parent, graph)

# Example graph as adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

primMST(graph)
