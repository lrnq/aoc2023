times = [59, 79 ,65, 75, 59796575]
distances = [597, 1234, 1032, 1328, 597123410321328]

ans_1 = 1
for i, time in enumerate(times):
    midpoint = time//2
    lo, hi = 0, midpoint
    while lo <= hi:
        mid = (lo+hi)//2
        if mid*(time-mid) > distances[i]:
            hi = mid-1
        else:
            lo = mid + 1
    if i < len(times)-1:
        ans_1 *= 2*(midpoint-lo+1)
    else:
        print("Part 1:", ans_1)
        print("Part 2:", 2*(midpoint-lo+1))
