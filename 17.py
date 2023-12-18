from aocd import get_data
from heapq import *

grid = [list(x) for x in get_data().splitlines()]
grid = [list(map(int, x)) for x in grid]

n, m = len(grid), len(grid[0])
dirs = [(0,1),(1,0),(0,-1),(-1,0)]


for part2 in 0,1:
    S = [(0,0,0,0,0,0)] # cost, x, y, dx, dy, dx-dy-count
    heapify(S)
    seen = set()
    while S:
        cost, x, y, dx, dy, cnt = heappop(S)
        if ((x,y) == (n-1, m-1) and not part2) or ((x,y) == (n-1, m-1) and part2 and cnt >= 4):
            print(f"Part {part2+1}:", cost)
            break
        if (x, y, dx, dy, cnt) in seen:
            continue
        seen.add((x,y,dx,dy,cnt))
        if cnt < (10 if part2 else 3) and (dx, dy) != (0,0):
            if 0 <= x+dx < n and 0 <= y+dy < m:
                heappush(S, (cost + grid[x+dx][y+dy], x+dx, y+dy, dx, dy, cnt+1))

        if not part2 or (cnt >= 4 or (dx, dy) == (0,0)):
            for xx, yy in dirs:
                if 0 <= x+xx < n and 0 <= y+yy < m:
                    if (xx, yy) not in [(-dx,-dy),(dx, dy)]:
                        heappush(S, (cost + grid[x+xx][y+yy], x+xx, y+yy, xx, yy, 1))
