from aocd import get_data

data = get_data().splitlines()


def shoelace(x, y):
    return abs(sum(x[i] * y[i + 1] - x[i + 1] * y[i] for i in range(len(x) - 1))) / 2


i2d = {"0": "R", "1": "D", "2": "L", "3": "U"}
step_func = {
    "R": lambda x, y, s: (x, y + s),
    "L": lambda x, y, s: (x, y - s),
    "U": lambda x, y, s: (x - s, y),
    "D": lambda x, y, s: (x + s, y),
}
for part2 in 0, 1:
    boundary = 1
    xs, ys = [0], [0]
    x, y = (0, 0)
    for line in data:
        direction, step_size, hex_code = line.split()
        if part2:
            step_size = int(hex_code[2:-2], 16)
            direction = i2d[hex_code[-2]]
        x, y = step_func[direction](x, y, int(step_size))
        xs.append(x)
        ys.append(y)
        boundary += int(step_size)

    area = shoelace(xs, ys)
    print(f"Part {part2+1}", int(area + 1 - boundary / 2 + boundary))
