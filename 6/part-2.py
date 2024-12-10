from enum import Enum


class Direction(tuple[int, int], Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    def turn_right(self):
        match self:
            case Direction.LEFT:
                return Direction.UP
            case Direction.UP:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.LEFT


def parse_input(lines):
    grid = []
    start = (0, 0)
    for y, line in enumerate(lines):
        grid.append(line.strip())
        if "^" in line:
            start = (line.index("^"), y)
    return grid, start


def is_inside(grid, pos):
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)


def is_wall(grid, pos):
    return is_inside(grid, pos) and grid[pos[1]][pos[0]] == "#"


def next_step(grid, pos, direction):
    x, y = pos[0], pos[1]
    next_pos = (x + direction.value[0], y + direction.value[1])
    while is_wall(grid, next_pos):
        direction = direction.turn_right()
        next_pos = (x + direction.value[0], y + direction.value[1])
    return next_pos, direction


def simulate_guard(grid, start):
    pos, direction, visited = start, Direction.UP, set()
    while is_inside(grid, pos):
        visited.add(pos)
        pos, direction = next_step(grid, pos, direction)
    return visited


def is_loop(grid, start):
    pos, direction, visited = start, Direction.UP, set()
    while is_inside(grid, pos):
        if (pos, direction) in visited:
            return True
        visited.add((pos, direction))
        pos, direction = next_step(grid, pos, direction)
    return False


def find_loops(grid, start):
    positions = simulate_guard(grid, start)
    positions.remove(start)
    for pos in positions:
        x, y = pos
        new_grid = list(grid)
        new_grid[y] = grid[y][:x] + "#" + grid[y][x + 1 :]
        assert new_grid[y][x] == "#"
        if is_loop(new_grid, start):
            yield pos


t_input = []
with open("test.txt") as file:
    t_input = [line.strip() for line in file]

input = []
with open("input.txt") as file:
    input = [line.strip() for line in file]
lab, start = parse_input(input)


t_lab, t_start = parse_input(t_input)

print(len(list(find_loops(t_lab, t_start))))
print(len(list(find_loops(lab, start))))
