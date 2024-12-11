from collections import defaultdict

data = "3028 78 973951 5146801 5 0 23533 857".split()
map = defaultdict(int)
for val in data:
    map[int(val)] = 1


def process(map):
    ans = defaultdict(int)
    for rune, amt in map.items():
        if rune == 0:
            ans[1] += amt
        elif len(str(rune)) % 2 == 0:
            mid = len(str(rune)) // 2
            ans[int(str(rune)[:mid])] += amt
            ans[int(str(rune)[mid:])] += amt
        else:
            ans[rune * 2024] += amt
    return ans


for blink in range(75):
    map = process(map)


print(sum(map.values()))
