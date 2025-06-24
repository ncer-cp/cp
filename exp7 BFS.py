from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()             # To track visited nodes
    queue = deque([start])      # Use deque for efficient pops from front

    print("BFS traversal starting from node", start, ":")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call BFS
bfs(graph, 'A')
