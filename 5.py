from aocd import get_data
from collections import defaultdict


def f(m, i):
    for k in m.keys():
        l, r = k
        if l <= i <= r:
            return m[k](i)
    return i

def g(maps, i):
    cur = i
    for m in maps:
        cur = f(m, cur)
    return cur


lines = get_data().split("\n\n")
seeds = list(map(int, lines[0].split(":")[1].split()))
maps = [defaultdict() for _ in range(7)]
inv_maps = [defaultdict() for _ in range(7)]
for i, line in enumerate(lines[1:]):
    mi = list(map(lambda x: list(map(int, x.split())), line.split("\n")[1:]))
    for dr, sr, r in mi: 
        maps[i][(sr, sr+r-1)] = lambda x, r=r, sr=sr, dr=dr: dr+(x-sr)
        inv_maps[i][(dr, dr+r-1)] = lambda x, r=r, sr=sr, dr=dr: sr+(x-dr)

print("Part 1:", min(g(maps, seed) for seed in seeds))
loc = 0
while 1:    
    seed = g(inv_maps[::-1], loc)
    for l, r in zip(seeds[::2], seeds[1::2]):
        if l <= seed < l+r:
            print("Part 2:", loc)
            exit()
    loc+=1
