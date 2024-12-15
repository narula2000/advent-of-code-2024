import time

WIDTH = 101
HEIGHT = 103

quadrant_counts = [0, 0, 0, 0]

robots = []

with open("input.txt") as file:
    for line in file:
        if not line.strip():
            continue

        position, velocity = line.split()
        pos_x, pos_y = map(int, position[2:].split(","))
        vel_x, vel_y = map(int, velocity[2:].split(","))
        robots.append(((pos_x, pos_y), (vel_x, vel_y)))

seconds_elapsed = 0
while True:
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    seconds_elapsed += 1

    collision_detected = False
    for robot in robots:
        (pos_x, pos_y), (vel_x, vel_y) = robot
        new_x = (pos_x + seconds_elapsed * vel_x) % WIDTH
        new_y = (pos_y + seconds_elapsed * vel_y) % HEIGHT

        grid[new_y][new_x] += 1
        if grid[new_y][new_x] > 1:
            collision_detected = True

    if not collision_detected:
        print("+" * 80)
        print(seconds_elapsed)
        for row in grid:
            print("".join(map(str, row)))
        time.sleep(0.3)
