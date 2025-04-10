def BellmanFord(graph, source):
    v = len(graph)
    edges = [(at, to, weight) for at in graph for to, weight in graph[at]]

    distance = [float('inf')] * v
    distance[source] = 0

    for _ in range(v - 1):
        for at, to, weight in edges:
            if distance[at] != float('inf') and distance[at] + weight < distance[to]:
                distance[to] = distance[at] + weight

    #Detect negative cycle
    for at, to, weight in edges:
        if distance[at] != float('inf') and distance[at] + weight < distance[to]:
            distance[to] = float('-inf')  # Mark as part of a negative cycle

    return "Graph contains a negative cycle", distance if float('-inf') in distance else distance


g = {
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

src = 0
result = BellmanFord(g, src)
print(result)

