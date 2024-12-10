from collections import deque

data = []
with open("input.txt", "r") as file:
    for line in file:
        data.append([int(char) for char in list(line.strip())])

t_data = []
with open("test.txt", "r") as file:
    for line in file:
        t_data.append([int(char) for char in list(line.strip())])


def get_neighbors(x, y, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    height = len(grid)
    width = len(grid[0])

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < height and 0 <= new_y < width:
            neighbors.append((new_x, new_y))

    return neighbors


def count_paths_to_trailhead(start_x, start_y, grid):
    visited, reachable_nines = set(), set()
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, current_height = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue

        for next_x, next_y in get_neighbors(x, y, grid):
            next_height = grid[next_x][next_y]

            if next_height == current_height + 1:
                queue.append((next_x, next_y, next_height))

    return reachable_nines


ans = 0
for x in range(len(t_data)):
    for y in range(len((t_data[0]))):
        if t_data[x][y] == 0:
            ans += len((count_paths_to_trailhead(x, y, t_data)))
print(ans)

ans = 0
for x in range(len(data)):
    for y in range(len((data[0]))):
        if data[x][y] == 0:
            ans += len((count_paths_to_trailhead(x, y, data)))
print(ans)
