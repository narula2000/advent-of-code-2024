WIDTH = 101
HEIGHT = 103

quadrant_counts = [0, 0, 0, 0]

with open("input.txt") as file:
    for line in file:
        if not line.strip():
            continue

        position, velocity = line.split()
        pos_x, pos_y = map(int, position[2:].split(","))
        vel_x, vel_y = map(int, velocity[2:].split(","))

        new_x = (pos_x + 100 * vel_x) % WIDTH
        new_y = (pos_y + 100 * vel_y) % HEIGHT

        if new_x == WIDTH // 2 or new_y == HEIGHT // 2:
            continue

        if new_x < WIDTH // 2 and new_y < HEIGHT // 2:
            quadrant_counts[0] += 1
        elif new_x > WIDTH // 2 and new_y < HEIGHT // 2:
            quadrant_counts[1] += 1
        elif new_x < WIDTH // 2 and new_y > HEIGHT // 2:
            quadrant_counts[2] += 1
        else:
            quadrant_counts[3] += 1

print(quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3])
