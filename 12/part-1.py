with open("input.txt", "r") as f:
    lines = f.read().splitlines()

data = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        data[x + y * 1j] = c


def flood_fill(grid, start):
    region = set([start])
    symbol = grid[start]
    queue = [start]
    while queue:
        pos = queue.pop()
        for d in [1, -1, 1j, -1j]:
            new_pos = pos + d
            if new_pos in grid and new_pos not in region and grid[new_pos] == symbol:
                region.add(new_pos)
                queue.append(new_pos)
    return region


regions = []

uncovered = set(data.keys())
while len(uncovered) > 0:
    start = uncovered.pop()
    region = flood_fill(data, start)
    uncovered -= region
    regions.append((data[start], region))


def get_area(region):
    return len(region[1])


def get_perimeter(region):
    perimeter = 0
    for pos in region[1]:
        for d in [1, -1, 1j, -1j]:
            new_pos = pos + d
            if new_pos not in region[1]:
                perimeter += 1
    return perimeter


price = 0
for region in regions:
    area, perimeter = get_area(region), get_perimeter(region)
    price += area * perimeter

print(price)
