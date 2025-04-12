def topological_sort(graph):
    visited_nodes = set()
    top_order = []

    def explore(node):
        if node in visited_nodes:
            return
        visited_nodes.add(node)
        for neighbor in graph[node]:
            explore(neighbor)
        top_order.append(node)

    for vertex in graph:
        if vertex not in visited_nodes:
            explore(vertex)

    return top_order[::-1]


dag = {
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

sorted_nodes = topological_sort(dag)
print("Topological Sort Order:", sorted_nodes)
