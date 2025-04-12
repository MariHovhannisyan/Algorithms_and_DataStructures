def topological_sort(graph):
    visited_nodes = set()
    topo_order = []

    def depth_first(node):
        if node not in visited_nodes:
            visited_nodes.add(node)
            for neighbor, _ in graph[node]:
                depth_first(neighbor)
            topo_order.append(node)

    for current_node in graph:
        if current_node not in visited_nodes:
            depth_first(current_node)

    return topo_order[::-1]


def find_longest_path(dag, start_node):
    #weights to negative
    neg_weight_graph = {
        node: [(neighbor, -weight) for neighbor, weight in edges]
        for node, edges in dag.items()
    }

    sorted_nodes = topological_sort(neg_weight_graph)

    max_distances = {node: float('-inf') for node in dag}
    max_distances[start_node] = 0

    for node in sorted_nodes:
        if max_distances[node] != float('-inf'):
            for neighbor, neg_weight in neg_weight_graph[node]:
                max_distances[neighbor] = max(max_distances[neighbor], max_distances[node] - neg_weight)

    #distances back to positive
    final_distances = {
        node: -dist if dist != float('-inf') else float('-inf')
        for node, dist in max_distances.items()
    }

    return final_distances


dag_graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}

start = 0
longest_paths = find_longest_path(dag_graph, start)
print("Longest paths from node", start, ":", longest_paths)
