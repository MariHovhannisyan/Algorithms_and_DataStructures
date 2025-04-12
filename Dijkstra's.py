def lazy_dijkstra(graph, source, target):
    num_nodes = len(graph)
    min_distance = [float('inf')] * num_nodes
    min_distance[source] = 0

    queue = [(source, 0)]

    while queue:
        #node in the queue with the smallest distance
        smallest_index = min(range(len(queue)), key=lambda i: queue[i][1])
        current_node, current_cost = queue.pop(smallest_index)

        if current_node == target:
            return current_cost

        if current_cost > min_distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            total_cost = current_cost + weight
            if total_cost < min_distance[neighbor]:
                min_distance[neighbor] = total_cost
                queue.append((neighbor, total_cost))

    return float('inf')  #if target is unreachable


graph_data = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}

try:
    start_node = int(input("Enter the starting node: "))
    end_node = int(input("Enter the target node: "))

    shortest_path_cost = lazy_dijkstra(graph_data, start_node, end_node)

    print(f"Shortest path cost from node {start_node} to node {end_node}: {shortest_path_cost}")
except ValueError:
    print("Enter valid integer node values.")
