from aocd import get_data
from collections import Counter
from itertools import count
 
data = get_data().splitlines()
matrix = [list(x) for x in data]
 
n, m = len(matrix), len(matrix[0])
 
# Part 1
mem = [[n + 1] * m]
for _ in range(n):
    mem.append([0] * m)
 
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "O":
            mem[i + 1][j] = mem[i][j] - 1
        if matrix[i][j] == "#":
            mem[i + 1][j] = n - i
        if matrix[i][j] == ".":
            mem[i + 1][j] = mem[i][j]
 
cnts = Counter()
ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "O":
            cnts[mem[i + 1][j]] += 1
print(sum(k * v for k, v in cnts.items()))
 
 
# Part 2 (+ part 1 if you want)
# ok then...
def tilt(matrix):
    transposed = tuple(["".join(r) for r in zip(*matrix)])
    split_groups = []
    for r in transposed:
        sub_groups = []
        for g in r.split("#"):
            sub_groups.append("".join(reversed(sorted(g))))
        split_groups.append("#".join(sub_groups))
    return tuple(row[::-1] for row in split_groups)
 
 
matrix = tuple([tuple(x) for x in data])
seen = {matrix}
array = [matrix]
 
for c in count():
    for _ in range(4):
        matrix = tilt(matrix)
    if matrix in seen:
        f = array.index(matrix)
        break
    seen.add(matrix)
    array.append(matrix)
 
matrix = array[(1000000000 - f) % (c + 1 - f) + f]
ans = 0
for i, r in enumerate(matrix):
    ans += r.count("O") * (len(matrix) - i)
print(ans)
