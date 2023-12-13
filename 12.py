from collections import Counter
from functools import lru_cache

from aocd import get_data

lines = get_data(day=12, year=2023).splitlines()


# Part 1
def validate(record, targets):
    group_sizes = []
    size = 0
    for x in record:
        if x == "#":
            size += 1
        else:
            if size != 0:
                group_sizes.append(size)
                size = 0
    if size != 0:
        group_sizes.append(size)
    return group_sizes == targets


ans = 0
for i, line in enumerate(lines):
    cs, ns = line.split()
    ns = [int(x) for x in ns.split(",")]
    # Just do a DFS constructing all possible sequences and then validate each.
    s = [(cs, 0)]
    while s:
        (cur, cur_idx) = s.pop()
        if cur_idx == len(cur):
            ans += validate(cur, ns)
        else:
            if cur[cur_idx] == "?":
                for p in [".", "#"]:
                    s.append((cur[:cur_idx] + p + cur[cur_idx + 1 :], cur_idx + 1))
            else:
                s.append((cur, cur_idx + 1))
print("Part 1:", ans)


# Both parts
# I guess I should have expected this :)
@lru_cache(maxsize=None)
def f(l, ns):
    if not l:
        return not ns
    if not ns:
        return "#" not in l

    ans = 0
    cur = l[0]
    if cur == "." or cur == "?":
        ans += f(l[1:], ns)
    if cur == "#" or cur == "?":
        nxt_block_size = ns[0]
        if (
            nxt_block_size <= len(l)
            and not l[:nxt_block_size].count(".")
            and (nxt_block_size == len(l) or l[nxt_block_size] != "#")
        ):
            ans += f(l[nxt_block_size + 1 :], ns[1:])
    return ans


for p, part2 in enumerate([0, 1], start=1):
    out = 0
    for i, line in enumerate(lines):
        cs, ns = line.split()
        ns = tuple([int(x) for x in ns.split(",")])
        if part2:
            cs = "?".join([cs] * 5)
            ns *= 5
        out += f(cs, ns)
    print(f"Part {p}:", out)
