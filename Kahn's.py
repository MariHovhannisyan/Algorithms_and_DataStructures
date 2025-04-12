from collections import deque

def kahn(adj_list):
    in_degree = {node: 0 for node in adj_list}
    for neighbors in adj_list.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    #nodes having zero in-degree
    zero_in_degree = deque([node for node, deg in in_degree.items() if deg == 0])
    sorted_order = []

    while zero_in_degree:
        current = zero_in_degree.popleft()
        sorted_order.append(current)
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return sorted_order


dag_graph = {
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

order = kahn(dag_graph)
print("Topological Order:", order)
