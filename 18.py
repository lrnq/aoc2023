from shapely import geometry
from aocd import get_data

data = get_data().splitlines()


i2d = {"0": "R", "1": "D", "2": "L", "3": "U"}
step_func = {
    "R": lambda x, y, s: (x, y + s),
    "L": lambda x, y, s: (x, y - s),
    "U": lambda x, y, s: (x - s, y),
    "D": lambda x, y, s: (x + s, y),
}
for part2 in 0, 1:
    cur_pos = (0, 0)
    edges = [(0, 0)]
    for line in data:
        x, y = cur_pos
        direction, step_size, hex_code = line.split()
        if part2:
            step_size = int(hex_code[2:-2], 16)
            direction = i2d[hex_code[-2]]
        cur_pos = step_func[direction](x, y, int(step_size))
        edges.append(cur_pos)

    polygon = geometry.Polygon(edges)
    print(f"Part {part2+1}", (polygon.area + 1) - (polygon.length // 2) + polygon.length)
