from aocd import get_data
from collections import Counter
 
blocks = get_data(day=13, year=2023).split("\n\n")
blocks = [x.splitlines() for x in blocks]
 
def count(block, mistakes):
    n = len(block)
    for i in range(1, n):
        m = 0
        bound = min(i, len(block)-i)
        for c in range(bound):
            for j in range(len(block[:i][c])):
                if block[:i][::-1][c][j] != block[i:][c][j]:
                    m += 1
        if mistakes == m:
            return i
 
 
for part2 in [0, 1]:
    ans = 0
    for block in blocks:
        rows = [list(x) for x in block]
        columns = list(zip(*rows))
        rc = count(rows, part2)
        cc = count(columns, part2)
        ans += (100 * rc) if rc is not None else cc 
    print(f"Part {part2+1}:", ans) 
 
