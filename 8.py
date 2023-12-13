from collections import Counter, defaultdict
from aocd import get_data
from itertools import cycle
import math

lines = get_data(day=8, year=2023).splitlines()
ops = lines[0].strip()

g = defaultdict(list)
for line in lines[2:]:
    data = line.replace("(", "").replace(")", "").split("=")
    src = data[0].strip()
    for n in data[1].split(","):
        g[src].append(n.strip())

def p(v, cond):
    steps = -1
    cur = v
    for op in cycle(ops):
        steps += 1
        if cond(cur):
            break
        if op == "L":
            cur = g[cur][0]
        elif op == "R":
            cur = g[cur][1]
    return steps


for part in [0, 1]:
    starting_nodes = [x for x in g if x[-1] == "A"] if part else ["AAA"]
    starting_nodes_steps = [0]*len(starting_nodes)
    cond = (lambda x: x=="ZZZ") if not part else (lambda x: x[-1] == "Z")
    for i, v in enumerate(starting_nodes):
        starting_nodes_steps[i] = p(v, cond)
    print(f"Part {part+1}:",math.lcm(*starting_nodes_steps))
    

