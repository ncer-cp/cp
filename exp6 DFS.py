# Depth First Search using Recursion

# Function for DFS
def dfs(graph, visited, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)

# Example graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # To keep track of visited nodes

# Start DFS from node 'A'
print("DFS traversal starting from node A:")
dfs(graph, visited, 'A')
