import string

from collections import defaultdict, deque
from aocd import get_data

data = get_data().strip().split(",")


def run(s):
    cur = 0
    for x in s:
        cur = ((cur + ord(x)) * 17) % 256
    return cur


print("Part 1:", sum(run(s) for s in data))

mem = defaultdict(lambda: defaultdict(int))
for s in data:
    s = deque(s)
    label = []
    while s[0] in string.ascii_lowercase:
        label.append(s.popleft())
    label = "".join(label)
    box_number = run(label)
    op = s.popleft()
    if op == "=":
        mem[box_number][label] = int("".join(s).strip())
    else:
        if label in mem[box_number]:
            mem[box_number].pop(label)
ans = 0
for k, v in mem.items():
    for j, (kk, vv) in enumerate(v.items(), start=1):
        ans += j * (k + 1) * vv

print("Part 2:", ans)
