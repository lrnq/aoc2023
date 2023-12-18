from collections import deque

from aocd import get_data
import numpy as np
import networkx as nx

# super bad solution but i wanted to try to use networkx for something.

lines = get_data().splitlines()
n, m = len(lines), len(lines[0])
row_weights = [0] * n
col_weights = [0] * m

for expand in [1, 999_999]:
    for i, line in enumerate(lines):
        if all(x == "." for x in line):
            row_weights[i] += expand

    expanded = np.array(list(map(list, lines)))
    for col in range(m):
        if all(expanded[:, col] == "."):
            col_weights[col] += expand

    galaxies = []
    for i in range(n):
        for j in range(m):
            if expanded[i][j] == "#":
                galaxies.append((i, j))

    gg = np.ones((n, m))
    for i in range(n):
        gg[i] = row_weights[i] + gg[i]
    for j in range(m):
        gg[:, j] = col_weights[j] + gg[:, j]

    s = 0
    G = nx.Graph()
    for i in range(n):
        for j in range(m):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    G.add_edge((i, j), (i + di, j + dj), weight=gg[i + di][j + dj])

    for i, galaxy1 in enumerate(galaxies):
        paths = nx.single_source_dijkstra_path_length(G, source=galaxy1)
        for j in range(i + 1, len(galaxies)):
            s += paths[galaxies[j]]
    print(s)
