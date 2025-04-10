from collections import deque

def minimal_steps(maze_map):
    rows, cols = len(maze_map), len(maze_map[0])
    visited_cells = [[False] * cols for _ in range(rows)]
    directions = [(-1,0), (1,0), (0,1), (0,-1)]

    for y in range(rows):
        for x in range(cols):
            if maze_map[y][x] == 'S':
                start_y, start_x = y, x

    queue = deque()
    queue.append((start_y, start_x, 0))
    visited_cells[start_y][start_x] = True

    while queue:
        y, x, steps = queue.popleft()

        if maze_map[y][x] == 'E':
            return steps

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < rows and 0 <= nx < cols:
                if not visited_cells[ny][nx] and maze_map[ny][nx] != '#':
                    queue.append((ny, nx, steps + 1))
                    visited_cells[ny][nx] = True

    return -1  #եթե ճանապարհ չկա

labyrinth = [
    ['S', '', '', '#', '', '', ''],
    ['', '#', '', '', '', '#', ''],
    ['', '#', '', '', '', '', ''],
    ['', '', '#', '#', '', '', ''],
    ['#', '', '#', 'E', '', '#', '']
]

result = minimal_steps(labyrinth)
print("Քայլերի նվազագույն քանակը՝", result)

