from collections import defaultdict
from itertools import permutations


def is_within_bounds(pair, bounds):
    x, y = pair
    rows, cols = bounds
    return 0 <= x < rows and 0 <= y < cols


seen = defaultdict(set)
X = 0
Y = 0
with open("input.txt", "r") as file:
    for y, line in enumerate(file):
        Y += 1
        line = line.strip()
        X = 0
        for x, char in enumerate(line):
            X += 1
            if char != ".":
                seen[char].add((x, y))

t_seen = defaultdict(set)
T_X = 0
T_Y = 0
with open("test.txt", "r") as file:
    for y, line in enumerate(file):
        T_Y += 1
        line = line.strip()
        T_X = 0
        for x, char in enumerate(line):
            T_X += 1
            if char != ".":
                t_seen[char].add((x, y))


def generate_pairs(lst):
    return list(permutations(lst, 2))


def find_antidote(pair, bounds):
    a, b = pair
    diff_x = a[0] - b[0]
    diff_y = a[1] - b[1]
    an_a = (a[0] + diff_x, a[1] + diff_y)
    an_b = (b[0] - diff_x, b[1] - diff_y)

    res = []
    if is_within_bounds(an_a, bounds):
        res.append(an_a)
    if is_within_bounds(an_b, bounds):
        res.append(an_b)
    return res


ans = set()
for vals in t_seen.values():
    pairs = generate_pairs(list(vals))
    for pair in pairs:
        for an in find_antidote(pair, (T_X, T_Y)):
            ans.add(an)

print(len(ans))


ans = set()
for vals in seen.values():
    pairs = generate_pairs(list(vals))
    for pair in pairs:
        for an in find_antidote(pair, (X, Y)):
            ans.add(an)

print(len(ans))
