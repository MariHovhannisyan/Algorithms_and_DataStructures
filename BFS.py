from collections import deque

def breadth_first_search(adj_list, start_node):
    visited_nodes = set()
    node_queue = deque([start_node])

    while node_queue:
        current = node_queue.popleft()
        if current not in visited_nodes:
            print(current, end=" ")
            visited_nodes.add(current)
            for neighbor in adj_list.get(current, []):
                if neighbor not in visited_nodes:
                    node_queue.append(neighbor)

graph = {
    0: [7, 9, 11],
    1: [],
    2: [12],
    3: [2, 4],
    4: [],
    5: [],
    6: [5],
    7: [6, 3, 11],
    8: [1, 12],
    9: [8, 10, 0],
    10: [1],
    11: [],
    12: [2]
}

try:
    starting_point = int(input("Starting node: "))
    if starting_point not in graph:
        print("Invalid starting node.")
    else:
        print("BFS starting from node", starting_point, "results in:")
        breadth_first_search(graph, starting_point)
except ValueError:
    print("Enter a valid integer node.")
