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
    memo = {}

    def dfs(row, col, next):
        if (row, col, next) in memo:
            return memo[(row, col, next)]

        if grid[row][col] == 9:
            return 1

        total_paths = 0

        for next_x, next_y in get_neighbors(row, col, grid):
            next_height = grid[next_x][next_y]
            if next_height == next + 1:
                total_paths += dfs(next_x, next_y, next_height)

        memo[(row, col, next)] = total_paths
        return total_paths

    return dfs(start_x, start_y, 0)


ans = 0
grid = t_data
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 0:
            rating = count_paths_to_trailhead(row, col, grid)
            ans += rating

print(ans)

ans = 0
grid = data
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 0:
            rating = count_paths_to_trailhead(row, col, grid)
            ans += rating

print(ans)
