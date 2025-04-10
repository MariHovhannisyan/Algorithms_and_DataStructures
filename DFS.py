def depth_first_search(adj_matrix, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(f"Visited: {node}")

    for adj, is_connected in enumerate(adj_matrix[node]):
        if is_connected and adj not in visited:
            depth_first_search(adj_matrix, adj, visited)

adj_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  #0
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  #1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  #2
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  #3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #4
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],  #5
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  #6
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],  #7
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  #8
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  #10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #11
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #12
]

print("DFS starting from node 0:")
depth_first_search(adj_matrix, 0)

