from collections import Counter, defaultdict
from aocd import get_data

lines = get_data(day=7, year=2023).splitlines()
hands = list(map(lambda x: (x.split()[0], int(x.split()[1])),  lines))
d ={1: "AKQJT98765432", 2: "AKQT98765432J"}

def get_rank(hand):
    cnts = [count for _, count in Counter(hand).most_common(2)]
    return 0 if 5 in cnts else 1 if 4 in cnts else 2 if cnts == [3, 2] else 3 if 3 in cnts else 4 if cnts.count(2) == 2 else 5 if 2 in cnts else 6


for part in [1,2]:
    ranks = defaultdict(list)
    for hand, bid in hands:
        h = hand.replace("J", next(x[0] for x in Counter(hand).most_common() if x[0] != "J") if any(c!="J" for c in hand) and part == 2 else "J")
        ranks[get_rank(h)].append((hand, bid))

    total, cur_rank = 0, 1
    for i in range(6, -1, -1):
        for _, b in sorted(ranks[i], key=lambda x: [-d[part].index(y) for y in x[0]]):
            total += b*cur_rank
            cur_rank += 1
    print(f"Part {part}:", total)
