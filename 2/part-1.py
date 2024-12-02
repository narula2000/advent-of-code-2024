data = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        row = line.split()
        data.append([int(val) for val in row])

count = 0
for row in data:
    seen = set()
    for i in range(len(row)-1):
        seen.add(row[i] - row[i+1])
    if seen <= {1, 2, 3} or seen <= {-1, -2, -3}:
        count += 1

print(count)

