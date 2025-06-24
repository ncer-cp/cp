from collections import deque

def is_bipartite(graph, V):
    color = [-1] * V  # -1 means no color assigned

    for start in range(V):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0  # Start with color 0

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]  # Alternate color
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

# Example: Adjacency list representation
V = 4
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

if is_bipartite(graph, V):
    print("Graph is Bipartite (Bi-coloring possible)")
else:
    print("Graph is NOT Bipartite (Bi-coloring not possible)")
