from itertools import permutations

# Number of cities
V = 4

# Example cost/distance matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Function to solve TSP
def travelling_salesman(graph, start=0):
    # Create list of cities excluding the start city
    cities = list(range(V))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    # Try all permutations of cities
    for perm in permutations(cities):
        cost = 0
        current = start

        # Calculate cost for current path
        for next_city in perm:
            cost += graph[current][next_city]
            current = next_city
        cost += graph[current][start]  # Return to start

        if cost < min_cost:
            min_cost = cost
            best_path = [start] + list(perm) + [start]

    print("Minimum cost:", min_cost)
    print("Best path:", ' -> '.join(map(str, best_path)))

# Run the function
travelling_salesman(graph)
