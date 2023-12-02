from aocd import get_data
from collections import defaultdict

lines = get_data().splitlines()
counts = defaultdict(lambda: 1)
ans_1, ans_2 = 0, 0
for i, line in enumerate(lines):
    l, r = line.split("|")
    l = set(map(int, l.split(":")[1].strip().split()))
    r = set(map(int, r.split()))
    ans_1 += int(2**(len(l&r)-1))
    ans_2 += counts[i]
    for _ in range(counts[i]):
        for j in range(i+1, i+1+len(l&r)):
            counts[j] += 1
print(ans_1)
print(ans_2)
