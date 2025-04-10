from collections import deque, defaultdict

def kahn_topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['J'],
    'C': ['F', 'I'],
    'D': ['G', 'E'],
    'E': ['K', 'H'],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

result = kahn_topological_sort(graph)
print(result)

