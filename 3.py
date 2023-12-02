from aocd import get_data
import math
import itertools
from collections import defaultdict

matrix = get_data().splitlines()
n, m = len(matrix), len(matrix[0])
dirs = list(itertools.product((-1, 0, 1), (-1, 0, 1)))

def f(idxs):
    for i, j in idxs:
        for di, dj in dirs:
            if not (-1<i+di<n and -1<j+dj<m) or (i+di,j+dj) in idxs:
                continue
            if matrix[i+di][j+dj] != ".": return True
    return False

def g(parts, i, j):
    seen = set()
    numbers = []
    for di, dj in dirs:
        if not (-1<i+di<n and -1<j+dj<m):
            continue
        if (t := (i+di, j+dj)) in parts and (e:=parts[t]) not in seen:
            numbers.append(e[0])
            seen.add(e)
    return 0 if len(numbers) < 2 else numbers[0]*numbers[1]

ans_1 = 0
parts = defaultdict(tuple)
for i in range(n):
    cur_number = defaultdict(str)
    for j in range(m):
        if (e:=matrix[i][j]).isdigit():
            cur_number[(i,j)] = e
        if cur_number and (not e.isdigit() or j == m-1):
            if f(cur_number.keys()):
                v = int(''.join(cur_number.values()))
                ans_1 += v
                for idx in (l := list(cur_number.keys())):
                    parts[idx] = (v, l[0][0])
            cur_number = defaultdict(list)

ans_2 = sum(gear_val(parts, i, j) for i in range(n) for j in range(m) if matrix[i][j] == "*")
print("Part 1:", ans_1)
print("Part 2:", ans_2)
