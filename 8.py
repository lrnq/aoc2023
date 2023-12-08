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
    neighbours = data[1].split(",")
    for n in neighbours:
        g[src].append(n.strip())

for part in [1, 2]:
    starting_nodes = [x for x in g if x[-1] == "A"] if part == 2 else ["AAA"]
    starting_nodes_steps = [0]*len(starting_nodes)
    for i, cur_node in enumerate(starting_nodes):
        steps = -1
        for op in cycle(seq):
            steps += 1
            if cur_node[-1] == "Z" and part == 2 or cur_node == "ZZZ" and part == 1: 
                break
            if op == "L":
                cur_node = g[cur_node][0]
            elif op == "R":
                cur_node = g[cur_node][1]
        
        starting_nodes_steps[i] = steps

    print(f"Part {part}:",math.lcm(*starting_nodes_steps))
    

