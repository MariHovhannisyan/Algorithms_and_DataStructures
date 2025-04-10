def depth_first_search(graph, node, visited_nodes, component_result):
    if visited_nodes[node] == True:
        return

    visited_nodes[node] = True
    component_result.append(node)

    #all neighbors of the current node
    for neighbor in graph[node]:
        if not visited_nodes[neighbor]:
            depth_first_search(graph, neighbor, visited_nodes, component_result)
    return component_result

def connected_components(graph):
    visited_nodes = {node: False for node in graph}
    components = []

    for node in graph:
        if not visited_nodes[node]:
            component = []
            depth_first_search(graph, node, visited_nodes, component)
            components.append(component)

    return components

graph = {
    0: [4, 8, 13, 14],
    1: [5],
    2: [9, 15],
    3: [9],
    4: [0, 8],
    5: [1, 16, 17],
    6: [7, 11],
    7: [6],
    8: [0, 4, 14],
    9: [2, 3, 15],
    10: [15],
    11: [6],
    12: [],
    13: [0, 14],
    14: [0, 13, 8],
    15: [2, 9, 10],
    16: [5],
    17: [5]
}

connected_components_list = connected_components(graph)
print(connected_components_list)

