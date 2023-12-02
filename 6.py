lines = """Time:        59     79     65     75
Distance:   597   1234   1032   1328""".splitlines()
times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))
times.append(int(''.join(list(map(str, times)))))
distances.append(int(''.join(list(map(str, distances)))))

ans_1, ans_2 = 1, 1
for i, time in enumerate(times):
    ways = 0
    for x in range(1, time+1):
        ways += x*(time-x) > distances[i]
    ans_1 *= ways if ways and i < len(times)-1 else 1
    ans_2 *= ways if ways and i == len(times)-1 else 1
print("Part 1:", ans_1)
print("Part 2:", ans_2)
