from aocd import get_data
from collections import Counter

data = get_data()
matrix = [list(x) for x in data.splitlines()]
n, m = len(matrix), len(matrix[0])

for part2 in [0, 1]:
    starting_rays = [[[((0, -1), (0, 1))]]]
    if part2:
        starting_rays = []
        for i in range(n):
            starting_rays.append([[((i, -1), (0, 1))]])
            starting_rays.append([[((n - 1 - i, n - i), (0, -1))]])
        for j in range(m):
            starting_rays.append([[((-1, j), (1, 0))]])
            starting_rays.append([[((m - j, m - j - 1), (-1, 0))]])

    best = 0
    for p in starting_rays:
        r = p.copy()
        cnts = Counter()
        seen = set()
        while r:
            path = r.pop()
            (x, y), (dx, dy) = path.pop()
            if 0 <= x < n and 0 <= y < m:
                cnts[(x, y, dx, dy)] += 1
                seen.add((x, y))
            if cnts[(x, y, dx, dy)] == 2:
                continue
            if 0 <= x + dx < n and 0 <= y + dy < m:
                e = matrix[x + dx][y + dy]
                if (
                    e == "."
                    or (e == "-" and (dx, dy) in [(0, 1), (0, -1)])
                    or (e == "|" and (dx, dy) in [(1, 0), (-1, 0)])
                ):
                    r.append(path + [((x + dx, y + dy), (dx, dy))])
                elif e == "/":
                    r.append(path + [((x + dx, y + dy), (-dy, -dx))])
                elif e == """\\""":
                    r.append(path + [((x + dx, y + dy), (dy, dx))])
                elif e == "|":
                    r.append(path + [((x + dx, y + dy), (-1, 0))])
                    r.append(path + [((x + dx, y + dy), (1, 0))])
                elif e == "-":
                    r.append(path + [((x + dx, y + dy), (0, 1))])
                    r.append(path + [((x + dx, y + dy), (0, -1))])
        best = max(best, len(seen))
    print(f"Part {part2+1}:", best)
