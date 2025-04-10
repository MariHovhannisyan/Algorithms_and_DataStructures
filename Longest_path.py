def topological_sort(graph):
    visited = set()
    order = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph[node]:
                dfs(neighbor)
            order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return order[::-1]

def longest_path_in_dag(graph, start):
    neg_graph = {u: [(v, -w) for v, w in edges] for u, edges in graph.items()}
    top_order = topological_sort(neg_graph)
    dist = {node: float('-inf') for node in neg_graph}
    dist[start] = 0

    for u in top_order:
        if dist[u] != float('-inf'):
            for v, neg_weight in neg_graph[u]:
                dist[v] = max(dist[v], dist[u] - neg_weight)

    return {node: -d if d != float('-inf') else float('-inf') for node, d in dist.items()}

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}

result = longest_path_in_dag(graph, 0)
print(result)
