from collections import Counter
from functools import lru_cache

from aocd import get_data

lines = get_data(day=12, year=2023).splitlines()


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
