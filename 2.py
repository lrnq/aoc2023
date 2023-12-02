from aocd import get_data
import math
from collections import defaultdict

ans_1, ans_2 = 0, 0
cubes = {"red":12,"green":13,"blue":14}
for line in get_data().splitlines():
    x = line.split(":")
    id = x[0].split()[-1]
    sets = x[1].split(";")
    add_game = 1
    max_seen = defaultdict(int)
    for s in sets:
        for y in s.split(","):
            n, c = y.split() 
            n = int(n)
            if n > cubes[c]:
                add_game=0
            max_seen[c] = max(max_seen[c], n)
    ans_1 += add_game * int(id)
    ans_2 += math.prod(max_seen.values())

print("Part 1", ans_1)
print("Part 2", ans_2)
