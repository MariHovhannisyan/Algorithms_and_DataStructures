import numpy as np

def initialize(graph):
    n = len(graph)
    dist = np.full((n, n), float('inf'))
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
    return dist


def floyd_warshall(graph):
    dist = initialize(graph)
    n = len(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    #Detect negative cycles
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = float('-inf')

    return dist


# Example usage
graph = [
    [0, 4, 1, float('inf')],
    [float('inf'), 0, 6, float('inf')],
    [4, 1, 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]

shortest_paths = floyd_warshall(graph)

print("All Pairs Shortest Paths:")
print(shortest_paths)

