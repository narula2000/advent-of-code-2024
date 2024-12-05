import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10**6)
ans = 0
D = open("input.txt").read().strip()

# E[x] is the set of pages that must come before x
# ER[x] is the set of pages that must come after x
E = defaultdict(set)
ER = defaultdict(set)
edges, queries = D.split("\n\n")
for line in edges.split("\n"):
    x, y = line.split("|")
    x, y = int(x), int(y)
    E[y].add(x)
    ER[x].add(y)

for query in queries.split("\n"):
    vs = [int(x) for x in query.split(",")]
    assert len(vs) % 2 == 1
    ok = True
    for i, x in enumerate(vs):
        for j, y in enumerate(vs):
            if i < j and y in E[x]:
                ok = False
    if not ok:
        good = []
        Q = deque([])
        D = {v: len(E[v] & set(vs)) for v in vs}
        for v in vs:
            if D[v] == 0:
                Q.append(v)
        while Q:
            x = Q.popleft()
            good.append(x)
            for y in ER[x]:
                if y in D:
                    D[y] -= 1
                    if D[y] == 0:
                        Q.append(y)
        ans += good[len(good) // 2]

print(ans)
