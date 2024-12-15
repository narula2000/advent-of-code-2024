import sys

sys.setrecursionlimit(1000000)

with open("input.txt") as file:
    input_data = file.read().strip()


def preprocess_grid(grid_input):
    processed_grid = []
    for row in grid_input:
        new_row = []
        for cell in row:
            if cell == "#":
                new_row.extend(["#", "#"])
            elif cell == "O":
                new_row.extend(["[", "]"])
            elif cell == ".":
                new_row.extend([".", "."])
            elif cell == "@":
                new_row.extend(["@", "."])
        processed_grid.append(new_row)
    return processed_grid


def process(grid, rows, cols, instructions):
    current_x, current_y = 0, 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                current_x, current_y = i, j
                break

    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    for move in instructions:
        dx, dy = directions[move]
        affected_cells = [(current_x, current_y)]
        index = 0
        invalid_move = False

        while index < len(affected_cells):
            x, y = affected_cells[index]
            next_x, next_y = x + dx, y + dy

            if grid[next_x][next_y] in "O[]":
                if (next_x, next_y) not in affected_cells:
                    affected_cells.append((next_x, next_y))
                if grid[next_x][next_y] == "[":
                    if (next_x, next_y + 1) not in affected_cells:
                        affected_cells.append((next_x, next_y + 1))
                if grid[next_x][next_y] == "]":
                    if (next_x, next_y - 1) not in affected_cells:
                        affected_cells.append((next_x, next_y - 1))
            elif grid[next_x][next_y] == "#":
                invalid_move = True
                break

            index += 1

        if invalid_move:
            continue

        new_grid = [[grid[i][j] for j in range(cols)] for i in range(rows)]
        for x, y in affected_cells:
            new_grid[x][y] = "."
        for x, y in affected_cells:
            new_grid[x + dx][y + dy] = grid[x][y]

        grid = new_grid
        current_x += dx
        current_y += dy

    result = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] not in "[O":
                continue
            result += 100 * i + j

    print(result)


# Input parsing
split_data = input_data.split("\n\n")
raw_grid, instructions = split_data[0], split_data[1].replace("\n", "")

grid = [list(row) for row in raw_grid.split("\n")]
processed_grid = preprocess_grid(grid)
rows, cols = len(processed_grid), len(processed_grid[0])
process(processed_grid, rows, cols, instructions)
