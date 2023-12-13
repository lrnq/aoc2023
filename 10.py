from collections import defaultdict
from aocd import get_data
import networkx as nx
from shapely.geometry import Polygon, Point

data = get_data(day=10, year=2023).splitlines()
n = len(data)
G = defaultdict(set)

directions = {
    "|": {"up", "down"},
    "-": {"left", "right"},
    "7": {"down", "left"},
    "F": {"down", "right"},
    "J": {"up", "left"},
    "L": {"up", "right"},
    "S": {"up", "down", "left", "right"},
}


def add_edge(i, j, dir):
    if dir == "up" and i - 1 > -1 and data[i - 1][j] in "|F7":
        G[(i, j)].add((i - 1, j))
    elif dir == "down" and i + 1 < n and data[i + 1][j] in "|LJ":
        G[(i, j)].add((i + 1, j))
    elif dir == "left" and j - 1 >= 0 and data[i][j - 1] in "-LF":
        G[(i, j)].add((i, j - 1))
    elif dir == "right" and j + 1 < n and data[i][j + 1] in "-J7":
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
# we cross that are orthogonal to the direction of the ray.
polygon = Polygon([u for (u, v) in cycle])
print("Part 2:", sum(Point(i, j).within(polygon) for (i, j) in all_tiles))
