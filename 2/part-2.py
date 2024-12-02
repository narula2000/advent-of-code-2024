data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        row = line.split()
        data.append([int(val) for val in row])


def is_safe(row):
    lst = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(lst) <= {1, 2, 3} or set(lst) <= {-1, -2, -3}:
        return True
    return False


lst = []
for row in data:
    _row = []
    for i in range(len(row)):
        _row.append(is_safe(row[:i] + row[i + 1 :]))
    lst.append(any(_row))

print(sum(lst))
