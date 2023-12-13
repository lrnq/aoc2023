from collections import defaultdict
from aocd import get_data
import networkx as nx
from shapely.geometry import Polygon, Point

data = get_data(day=10, year=2023).splitlines()
n = len(data)
G = defaultdict(set)

directions = {
    "|": {"U", "D"},
    "-": {"L", "R"},
    "7": {"D", "L"},
    "F": {"D", "R"},
    "J": {"U", "L"},
    "L": {"U", "R"},
    "S": {"U", "D", "L", "R"},
}


def add_edge(i, j, dir):
    if dir == "U" and i - 1 > -1 and data[i - 1][j] in "|F7":
        G[(i, j)].add((i - 1, j))
    elif dir == "D" and i + 1 < n and data[i + 1][j] in "|LJ":
        G[(i, j)].add((i + 1, j))
    elif dir == "L" and j - 1 >= 0 and data[i][j - 1] in "-LF":
        G[(i, j)].add((i, j - 1))
    elif dir == "R" and j + 1 < n and data[i][j + 1] in "-J7":
        G[(i, j)].add((i, j + 1))


for i in range(n):
    for j in range(n):
        if (e := data[i][j]) in directions:
            [add_edge(i, j, dir) for dir in directions[e]]
            if e == "S":
                src = (i, j)

cycle = nx.find_cycle(nx.Graph(G), source=src)
print("Part 1", len(cycle) // 2)
# This is overkill. Since the polygon is rectilinear we can just shoot a ray in either orthogonal direction and count the number of tiles
# we cross that are orthogonal to the direction of the ray. This would also work for simple polygons, but it requires more work.
print("Part 2:", sum(Point(i, j).within(Polygon([u for (u, v) in cycle])) for i in range(n) for j in range(n)))
