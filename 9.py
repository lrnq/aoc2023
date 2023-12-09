from aocd import get_data


def f(s):
    rows = [s]
    while any(rows[-1]):
        rows.append([rows[-1][i] - rows[-1][i - 1] for i in range(1, len(rows[-1]))])
    return sum(rows[i][-1] for i in range(len(rows) - 2, -1, -1))


lines = get_data().splitlines()
print(sum(f([int(x) for x in s.split()]) for s in lines))
print(sum(f([int(x) for x in s.split()][::-1]) for s in lines))
