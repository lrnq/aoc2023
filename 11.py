from collections import deque

from aocd import get_data


# Note: Computing the manhattan distance between all pairs of galaxies is much faster.
lines = get_data(day=11, year=2023).splitlines()
n, m = len(lines), len(lines[0])
galaxies = [(i, j) for i in range(n) for j in range(m) if lines[i][j] == "#"]
for c, expand in enumerate([1, 999_999], start=1):
    row_weights = [expand if all(lines[i][j] == "." for j in range(m)) else 0 for i in range(n)]
    col_weights = [expand if all(lines[j][i] == "." for j in range(n)) else 0 for i in range(m)]
    seen = set()
    sum_of_paths = 0
    for i, g in enumerate(galaxies):
        seen.add(g)
        q = deque([(*g, 0)])
        tmp = set(g)
        while q:
            x, y, d = q.popleft()
            if (x, y) not in seen:
                if lines[x][y] == "#":
                    sum_of_paths += d
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= x + di < n and 0 <= y + dj < m and (x + di, y + dj) not in tmp:
                    q.append((x + di, y + dj, d + 1 + row_weights[x + di] + col_weights[y + dj]))
                    tmp.add((x + di, y + dj))
    print(f"Part {c}:", sum_of_paths)
