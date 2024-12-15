with open("input.txt") as file:
    lines = [line.strip() for line in file]


tokens = 0
prefix = 10000000000000
for line in lines:
    if line.startswith("Button"):
        sections = line.split(" ")
        a = sections[1].split(":")[0]
        if a == "A":
            x1 = int(sections[2][2:-1])
            y1 = int(sections[3][2:])
        else:
            x2 = int(sections[2][2:-1])
            y2 = int(sections[3][2:])

    elif line.startswith("Prize"):
        sections = line.split(" ")
        x = int(sections[1][2:-1]) + prefix
        y = int(sections[2][2:]) + prefix
        a = (x * y2 - y * x2) / (x1 * y2 - y1 * x2)
        b = (y * x1 - x * y1) / (x1 * y2 - y1 * x2)
        if a == int(a) and b == int(b):
            tokens += int(3 * a + b)

print(tokens)
