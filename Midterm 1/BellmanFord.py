def bellman_ford(graph, start_node):
    num_vertices = len(graph)
    all_edges = [(u, v, w) for u in graph for v, w in graph[u]]

    distances = [float('inf')] * num_vertices
    distances[start_node] = 0

    for _ in range(num_vertices - 1):
        for u, v, w in all_edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    #negative weight cycles
    for u, v, w in all_edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            distances[v] = float('-inf')  # Mark involvement in negative cycle

    if float('-inf') in distances:
        return "Graph contains a negative cycle", distances
    return "No negative cycle detected", distances


graph_data = {
    0: [(1, 5)],
    1: [(6, 60), (5, 30), (2, 20)],
    2: [(3, 10), (4, 75)],
    3: [(2, -15)],
    4: [(9, 100)],
    5: [(6, 5), (8, 50)],
    6: [(7, -50)],
    7: [(8, -10)],
    8: [],
    9: []
}

start = 0
status, shortest_distances = bellman_ford(graph_data, start)

print(status)
print("Shortest distances from node", start, ":", shortest_distances)
