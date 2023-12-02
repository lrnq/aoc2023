from collections import Counter, defaultdict
from aocd import get_data

lines = get_data().splitlines()
hands = list(map(lambda x: (x.split()[0], int(x.split()[1])),  lines))
d ={1: "AKQJT98765432", 2: "AKQT98765432J"}

def get_rank(hand):
    cnts = Counter(hand).most_common(2)
    match cnts:
        case [(_, 5)]:
            return 0
        case [(_, 4), (_, 1)]:
            return 1
        case [(_, 3), (_, 2)]:
            return 2
        case [(_, 3), _]:
            return 3
        case [(_, 2), (_, 2)]:
            return 4
        case [(_, 2), _]:
            return 5
        case _:
            return 6

for part in [1,2]:
    cards = d[part]
    ranks = defaultdict(list)
    for hand, bid in hands:
        best = get_rank(hand) if part == 1 else min([get_rank(hand.replace("J", c)) for c in cards])
        ranks[best].append((hand, bid))
    total = 0
    cur_rank = 1
    for i in range(6, -1, -1):
        x = sorted(ranks[i], key=lambda x: [-cards.index(y) for y in x[0]])
        for _, b in x:
            total += b*cur_rank
            cur_rank += 1
    print(f"Part {part}:", total)
