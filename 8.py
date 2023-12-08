from collections import Counter, defaultdict
from aocd import get_data
from itertools import cycle
import math

lines = get_data(day=8, year=2023).splitlines()
seq = lines[0].strip()

g = defaultdict(list)
for line in lines[2:]:
    data = line.replace("(", "").replace(")", "").split("=")
    src = data[0].strip()
    for n in data[1].split(","):
        g[src].append(n.strip())

def p(v, cond):
    steps = -1
    cur = v
    for op in cycle(seq):
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
    for i, v in enumerate(starting_nodes):
        cond = (lambda x: x=="ZZZ") if not part else (lambda x: x[-1] == "Z")
        starting_nodes_steps[i] = p(v, cond)
    print(f"Part {part+1}:",math.lcm(*starting_nodes_steps))
    

# You can verify that LCM works by checking the input has #starting-nodes disjoint 2-regular graphs with the necessary properties.
C = defaultdict(list)
for src in g:
    if src[-1] != "A":
        continue
    steps = 0
    c = 0
    cur = src
    for op in cycle(seq):
        steps += 1
        if cur[-1] == "Z":
            C[src].append(steps)
            steps = 0
            c += 1
            if c == 2:
                break
        if op == "L":
            cur = g[cur][0]
        elif op == "R":
            cur = g[cur][1]
reference_dist = C["AAA"][0] - C["AAA"][1]
for k in C.keys():
    if k == "AAA":
        assert C[k][0] - C[k][1] == reference_dist


        



