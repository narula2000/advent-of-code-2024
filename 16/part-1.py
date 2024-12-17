import heapq


class MinHeap:
    """Min heap implementation using heapq."""

    def __init__(self):
        self.heap = []

    def insert(self, element):
        heapq.heappush(self.heap, element)

    def extract_min(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_in_bounds(x, y, width, height, grid):
    return 0 <= x < width and 0 <= y < height and grid[y][x] != "#"


def dijkstra(graph, start, directionless):
    queue = MinHeap()
    distances = {}

    start_key = f"{start['x']},{start['y']}" + (",0" if not directionless else "")
    queue.insert((0, start_key))
    distances[start_key] = 0

    while queue:
        current_score, current_node = queue.extract_min()

        if distances.get(current_node, float("inf")) < current_score:
            continue

        for next_node, weight in graph.get(current_node, {}).items():
            new_score = current_score + weight
            if new_score < distances.get(next_node, float("inf")):
                distances[next_node] = new_score
                queue.insert((new_score, next_node))

    return distances


def parse_grid(grid):
    width, height = len(grid[0]), len(grid)
    start, end = {"x": 0, "y": 0}, {"x": 0, "y": 0}
    forward, reverse = {}, {}

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                start = {"x": x, "y": y}
            if cell == "E":
                end = {"x": x, "y": y}

            if cell != "#":
                for i, (dx, dy) in enumerate(DIRECTIONS):
                    nx, ny = x + dx, y + dy
                    key = f"{x},{y},{i}"
                    move_key = f"{nx},{ny},{i}"

                    if is_in_bounds(nx, ny, width, height, grid):
                        forward.setdefault(key, {})[move_key] = 1
                        reverse.setdefault(move_key, {})[key] = 1

                    for rotate_key in [
                        f"{x},{y},{(i + 3) % 4}",
                        f"{x},{y},{(i + 1) % 4}",
                    ]:
                        forward.setdefault(key, {})[rotate_key] = 1000
                        reverse.setdefault(rotate_key, {})[key] = 1000

    for i in range(len(DIRECTIONS)):
        rotate_key = f"{end['x']},{end['y']},{i}"
        key = f"{end['x']},{end['y']}"
        forward.setdefault(rotate_key, {})[key] = 0
        reverse.setdefault(key, {})[rotate_key] = 0

    return {"start": start, "end": end, "forward": forward, "reverse": reverse}


with open("input.txt") as file:
    grid = file.read().strip().split("\n")
parsed = parse_grid(grid)
distances = dijkstra(parsed["forward"], parsed["start"], False)
end_key = f"{parsed['end']['x']},{parsed['end']['y']}"
print(distances.get(end_key, float("inf")))
