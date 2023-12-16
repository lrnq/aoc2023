# Notes: You could speed this up by turning it into a variant of finding the largest palindrome substring with the bound constraints. 
 
from aocd import get_data
from collections import Counter
 

blocks = get_data(day=13, year=2023).split("\n\n")
blocks = [x.splitlines() for x in blocks]
 
def count(block, mistakes):
    n, m = len(block), len(block[0])
    for i in range(1, n):
        miss = 0
        bound = min(i, n-i)
        for c in range(bound):
            for j in range(m):
                if block[:i][::-1][c][j] != block[i:][c][j]:
                    miss += 1
        if mistakes == miss:
            return i
 
 
for part2 in [0, 1]:
    ans = 0
    for block in blocks:
        rc = count([list(x) for x in block], part2)
        cc = count(list(zip(*rows)), part2)
        ans += (100 * rc) if rc is not None else cc 
    print(f"Part {part2+1}:", ans) 
 
