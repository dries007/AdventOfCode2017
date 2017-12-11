# Thanks https://www.redblobgames.com/grids/hexagons/

_dir = {
    #      x   y  z
    'n':  (0, 1, -1),
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
    's':  (0, -1, 1),
    'sw': (-1, 0, 1),
    'nw': (-1, 1, 0)
}


def parse(data):
    return [_dir[x] for x in data.split(',')]


def dist(x, y, z):
    return int((abs(x) + abs(y) + abs(z)) / 2)


def part1(data):
    data = parse(data)
    x, y, z = 0, 0, 0
    for d in data:
        x += d[0]
        y += d[1]
        z += d[2]
    print(x, y, z)
    print((x-y), (y-z), (z-x))

    return dist(x, y, z)


def part2(data):
    data = parse(data)
    m = 0
    x, y, z = 0, 0, 0
    for d in data:
        x += d[0]
        y += d[1]
        z += d[2]
        m = max(dist(x, y, z), m)
    print(x, y, z)
    print((x-y), (y-z), (z-x))

    return m


if __name__ == '__main__':
    print("example1 (3):", part1(r'ne,ne,ne'))
    print("example1 (0):", part1(r'ne,ne,sw,sw'))
    print("example1 (2):", part1(r'ne,ne,s,s'))
    print("example1 (3):", part1(r'se,sw,se,sw,sw'))
    # print("example2:", part2(example_data))
    input_data = r'ne,se,se,s,nw,s,ne,sw,s,nw,sw,sw,sw,sw,sw,s,sw,nw,nw,nw,nw,ne,nw,nw,n,n,n,nw,nw,nw,n,n,s,nw,sw,se,n,n,ne,n,n,n,sw,n,ne,n,nw,n,sw,n,se,n,ne,ne,sw,n,n,ne,ne,ne,ne,s,se,ne,ne,ne,n,ne,ne,ne,sw,ne,ne,sw,se,se,ne,sw,nw,se,s,nw,se,nw,se,se,se,se,se,ne,se,se,n,n,se,se,sw,se,se,se,se,se,se,se,se,se,ne,se,ne,se,se,s,se,se,se,se,se,s,se,ne,s,se,s,se,ne,s,se,s,s,s,se,se,s,s,nw,s,s,s,se,s,s,s,s,nw,nw,s,s,nw,s,s,nw,s,s,s,s,s,s,s,nw,s,sw,s,s,sw,s,s,s,s,s,ne,nw,s,s,n,s,sw,s,n,sw,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,s,s,se,se,sw,sw,nw,s,s,s,s,sw,sw,sw,ne,s,sw,s,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,se,se,sw,sw,sw,sw,sw,sw,sw,nw,nw,sw,sw,nw,nw,s,sw,sw,sw,sw,se,sw,s,nw,se,sw,nw,sw,sw,sw,sw,sw,sw,nw,nw,sw,sw,sw,sw,sw,n,n,nw,sw,sw,nw,se,sw,nw,sw,ne,sw,nw,n,n,nw,sw,nw,nw,nw,nw,nw,sw,n,nw,nw,sw,nw,n,nw,sw,nw,s,sw,sw,sw,nw,nw,sw,nw,nw,nw,sw,sw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,ne,nw,ne,nw,nw,sw,nw,nw,se,nw,nw,se,nw,nw,nw,sw,n,n,nw,n,nw,nw,sw,nw,n,nw,s,nw,nw,ne,nw,nw,nw,nw,nw,n,nw,n,nw,nw,nw,se,nw,nw,n,se,n,ne,nw,nw,nw,nw,nw,nw,n,nw,nw,nw,n,nw,ne,n,nw,se,n,nw,se,nw,n,n,s,nw,n,n,n,ne,sw,n,se,nw,nw,nw,nw,nw,n,n,nw,n,nw,nw,nw,n,n,nw,s,nw,nw,nw,nw,n,n,sw,n,n,nw,nw,se,nw,ne,nw,n,nw,se,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,nw,s,s,ne,nw,nw,ne,sw,nw,se,n,se,ne,ne,nw,nw,n,nw,s,n,se,n,n,n,n,n,n,n,n,n,n,n,n,nw,n,n,n,n,nw,n,se,n,n,sw,n,n,ne,s,n,n,n,n,n,n,n,n,n,s,n,nw,n,n,ne,s,n,ne,se,n,n,ne,ne,n,s,s,n,n,nw,n,n,s,ne,n,n,n,ne,ne,n,se,n,n,n,n,sw,n,sw,n,se,s,nw,n,n,n,ne,n,ne,n,ne,se,s,se,ne,n,n,n,ne,ne,ne,ne,ne,ne,n,ne,n,n,ne,n,n,se,ne,n,n,n,n,se,ne,n,n,n,se,s,ne,ne,ne,ne,ne,ne,ne,sw,sw,ne,ne,ne,nw,n,ne,n,ne,ne,ne,n,ne,ne,sw,ne,n,se,ne,nw,ne,n,s,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,ne,sw,s,n,ne,n,ne,ne,ne,n,nw,sw,ne,ne,ne,ne,ne,ne,se,ne,n,s,ne,sw,nw,ne,n,ne,n,n,ne,n,ne,ne,ne,s,ne,ne,ne,ne,ne,ne,se,ne,ne,ne,ne,ne,ne,s,ne,se,n,ne,sw,ne,n,ne,ne,ne,ne,ne,ne,s,ne,ne,ne,ne,se,ne,s,ne,ne,ne,ne,s,ne,ne,s,ne,ne,ne,ne,ne,ne,ne,se,se,se,ne,ne,n,ne,ne,ne,s,n,ne,s,ne,se,ne,ne,ne,ne,ne,s,sw,ne,s,ne,se,se,ne,nw,ne,se,se,se,ne,nw,sw,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,se,ne,ne,se,s,se,ne,se,ne,nw,s,se,ne,ne,se,se,se,s,ne,se,ne,sw,se,ne,se,se,ne,ne,ne,se,se,ne,se,nw,s,ne,ne,n,ne,ne,se,ne,ne,se,ne,ne,se,ne,ne,ne,se,ne,nw,ne,ne,sw,se,se,sw,se,ne,ne,se,nw,sw,ne,s,ne,ne,se,ne,ne,s,se,ne,ne,ne,n,sw,n,se,ne,ne,ne,se,n,ne,sw,ne,sw,se,se,ne,ne,se,ne,ne,se,se,se,se,nw,nw,se,se,ne,se,sw,ne,s,ne,ne,se,se,se,sw,sw,se,ne,ne,nw,n,ne,se,ne,ne,se,se,se,ne,ne,sw,se,ne,se,ne,se,se,se,se,ne,se,se,se,ne,se,se,sw,se,se,se,se,se,ne,se,se,se,se,se,ne,se,se,se,se,se,ne,ne,sw,se,se,ne,ne,ne,nw,se,se,nw,se,se,se,sw,se,se,se,sw,ne,se,se,sw,se,s,se,se,se,se,se,se,s,se,se,s,s,se,se,se,se,se,se,se,sw,se,se,se,se,se,se,ne,n,se,se,n,se,se,se,sw,s,ne,s,se,se,se,se,se,se,se,se,sw,ne,se,se,s,se,se,se,se,s,n,se,se,nw,se,ne,se,se,nw,se,se,se,se,n,se,se,se,se,se,se,se,se,n,se,se,se,se,n,se,s,se,n,s,se,s,s,sw,se,s,se,n,se,sw,s,se,sw,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,sw,n,sw,se,se,se,s,se,nw,se,s,s,s,se,s,se,se,sw,sw,se,se,ne,se,s,se,s,se,ne,s,s,se,s,nw,se,se,s,sw,s,se,s,s,se,s,s,sw,nw,se,se,se,sw,s,nw,se,n,se,s,s,s,se,se,se,se,ne,ne,s,s,se,se,sw,s,s,se,se,nw,s,nw,s,se,s,s,s,se,se,s,s,s,nw,n,sw,se,se,s,se,se,se,se,se,s,s,se,se,s,s,s,s,se,sw,se,ne,nw,sw,ne,s,s,s,se,n,nw,se,se,se,s,se,ne,sw,s,s,se,s,s,s,nw,nw,s,s,se,s,s,se,s,s,s,sw,s,se,se,ne,s,se,s,nw,s,se,s,se,se,s,s,nw,n,se,n,se,s,s,se,se,se,s,se,s,s,sw,s,s,nw,se,sw,s,sw,s,s,s,se,se,n,s,se,s,ne,s,s,se,s,se,se,s,nw,s,s,s,n,se,sw,s,s,se,ne,s,s,s,n,s,s,s,s,nw,s,s,s,n,s,se,s,s,s,se,s,s,s,s,s,n,s,s,se,se,s,ne,se,se,s,s,ne,s,s,s,se,se,se,nw,s,s,se,s,se,s,s,s,s,s,s,se,s,s,s,s,s,n,s,s,ne,n,s,s,s,s,n,n,ne,se,s,sw,s,s,s,s,s,s,s,ne,s,s,se,s,se,se,s,s,s,s,s,ne,s,s,sw,s,se,nw,s,s,sw,s,s,s,sw,s,s,s,s,s,se,nw,s,s,s,s,s,sw,s,s,s,s,sw,s,nw,ne,se,s,ne,s,s,s,nw,s,s,s,s,se,s,s,sw,s,s,s,s,s,s,s,se,s,sw,ne,s,s,s,s,sw,sw,sw,s,nw,s,ne,s,s,s,n,sw,sw,s,sw,sw,s,se,s,s,se,s,s,s,s,sw,s,s,sw,s,s,s,s,nw,sw,s,s,sw,s,s,se,nw,s,s,s,s,s,nw,s,sw,s,s,n,s,s,s,n,sw,se,s,se,s,se,s,s,sw,sw,n,sw,s,s,se,s,sw,sw,se,s,nw,s,sw,s,s,s,nw,s,s,s,s,sw,nw,sw,s,s,s,s,s,s,s,s,nw,s,sw,sw,sw,s,sw,n,s,sw,n,sw,s,sw,sw,s,s,s,sw,s,s,n,n,s,sw,s,sw,s,s,sw,nw,s,se,s,s,s,n,s,s,se,sw,s,s,sw,s,s,sw,s,sw,sw,s,s,s,sw,s,s,s,s,s,sw,sw,sw,se,n,s,sw,sw,sw,s,n,se,s,s,sw,s,s,sw,sw,se,se,sw,sw,sw,s,s,s,sw,s,sw,s,s,sw,sw,sw,se,s,sw,s,sw,sw,sw,se,sw,sw,sw,n,sw,sw,s,s,s,sw,s,sw,sw,s,sw,ne,s,sw,s,s,sw,s,s,n,sw,s,s,sw,se,s,s,n,sw,sw,s,s,s,s,sw,nw,se,sw,sw,sw,s,sw,s,sw,s,sw,s,sw,s,nw,s,s,sw,sw,s,s,sw,nw,ne,sw,sw,sw,sw,ne,s,s,sw,s,sw,sw,s,sw,sw,s,sw,sw,sw,sw,s,sw,ne,sw,sw,s,nw,sw,s,s,s,s,sw,sw,se,ne,nw,sw,sw,sw,s,s,se,s,s,sw,s,sw,sw,s,n,ne,sw,sw,s,sw,s,sw,s,sw,s,sw,sw,sw,sw,s,sw,s,sw,sw,s,nw,s,nw,s,sw,sw,sw,sw,s,sw,sw,s,sw,sw,s,se,s,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,sw,se,s,s,sw,sw,s,s,sw,sw,sw,s,sw,s,sw,sw,s,sw,sw,ne,sw,s,sw,s,sw,sw,sw,sw,s,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,s,sw,sw,sw,nw,sw,sw,sw,se,n,sw,sw,s,s,sw,sw,sw,s,sw,sw,sw,nw,sw,sw,nw,sw,sw,sw,sw,s,n,sw,s,sw,sw,sw,s,sw,se,sw,sw,sw,ne,sw,sw,sw,s,sw,sw,sw,n,sw,sw,s,sw,sw,s,sw,sw,s,se,s,sw,sw,sw,ne,sw,sw,sw,n,sw,sw,sw,sw,sw,sw,ne,se,sw,sw,n,sw,sw,sw,sw,se,sw,sw,nw,sw,n,sw,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,nw,sw,se,sw,sw,sw,s,n,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,ne,sw,se,sw,se,sw,sw,sw,sw,sw,s,sw,nw,n,se,sw,ne,sw,sw,sw,n,s,se,sw,se,sw,se,n,s,sw,sw,sw,nw,n,se,sw,sw,nw,sw,sw,ne,sw,sw,s,sw,sw,s,sw,sw,sw,nw,s,sw,s,s,sw,ne,sw,sw,sw,sw,nw,sw,s,sw,nw,sw,nw,s,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,ne,sw,s,sw,sw,sw,sw,nw,sw,sw,nw,sw,sw,nw,sw,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,s,sw,se,s,sw,sw,nw,sw,sw,n,se,sw,s,sw,sw,sw,nw,sw,sw,sw,sw,sw,nw,nw,nw,sw,sw,sw,sw,sw,n,se,sw,sw,n,nw,sw,sw,n,sw,n,sw,sw,sw,sw,nw,se,nw,sw,sw,sw,ne,sw,nw,nw,sw,sw,sw,sw,sw,nw,sw,nw,nw,nw,sw,sw,sw,ne,sw,sw,sw,se,sw,nw,ne,sw,sw,sw,nw,sw,sw,n,sw,nw,nw,nw,nw,sw,sw,sw,sw,sw,se,sw,sw,ne,sw,s,sw,sw,sw,sw,sw,sw,sw,sw,ne,nw,sw,sw,nw,se,nw,sw,sw,sw,sw,sw,nw,nw,sw,sw,sw,ne,sw,nw,sw,sw,sw,nw,sw,sw,sw,sw,ne,n,nw,sw,sw,nw,sw,nw,n,sw,sw,sw,ne,sw,sw,sw,nw,sw,nw,sw,nw,sw,sw,nw,se,sw,sw,nw,nw,nw,nw,nw,nw,n,sw,sw,s,sw,sw,sw,s,se,sw,n,sw,se,nw,sw,sw,sw,sw,nw,nw,nw,se,sw,ne,sw,n,sw,se,sw,nw,nw,sw,nw,sw,sw,sw,ne,sw,n,nw,sw,nw,se,sw,ne,se,nw,sw,nw,se,sw,nw,sw,se,n,nw,se,sw,n,se,sw,nw,se,s,sw,sw,nw,sw,sw,sw,nw,sw,s,nw,ne,nw,sw,n,nw,nw,ne,ne,nw,ne,sw,nw,sw,nw,nw,nw,nw,sw,sw,se,sw,nw,sw,nw,sw,sw,sw,nw,nw,ne,nw,sw,sw,se,sw,nw,sw,sw,sw,sw,se,sw,ne,nw,sw,sw,nw,nw,nw,sw,se,sw,nw,sw,sw,sw,nw,sw,sw,se,sw,nw,sw,ne,sw,sw,nw,nw,sw,sw,ne,nw,sw,s,sw,sw,sw,nw,nw,n,nw,nw,sw,sw,sw,sw,sw,nw,nw,nw,nw,nw,nw,nw,sw,n,nw,sw,sw,n,nw,nw,sw,s,sw,ne,se,nw,nw,nw,sw,nw,sw,nw,s,nw,nw,n,s,nw,s,nw,sw,sw,nw,nw,nw,nw,nw,nw,se,nw,se,nw,nw,s,sw,nw,nw,nw,se,nw,nw,sw,sw,nw,sw,nw,sw,nw,s,nw,nw,nw,nw,sw,nw,ne,n,nw,nw,nw,sw,nw,nw,nw,sw,ne,nw,sw,nw,sw,nw,nw,nw,nw,nw,nw,s,nw,nw,ne,nw,nw,nw,n,sw,nw,nw,nw,nw,se,nw,sw,nw,sw,nw,nw,se,nw,nw,se,nw,sw,sw,sw,nw,sw,s,nw,nw,nw,s,nw,nw,se,sw,nw,sw,se,nw,ne,nw,nw,n,nw,nw,sw,nw,nw,ne,nw,ne,s,nw,sw,nw,nw,nw,nw,nw,sw,sw,sw,nw,sw,n,nw,nw,n,sw,sw,nw,ne,se,sw,nw,n,nw,nw,ne,nw,sw,se,sw,sw,n,nw,ne,nw,nw,sw,n,nw,sw,nw,ne,n,n,nw,nw,sw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,sw,se,nw,nw,s,nw,sw,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,sw,sw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,sw,nw,nw,n,n,nw,nw,ne,nw,nw,nw,n,sw,nw,sw,se,s,nw,nw,nw,s,nw,nw,nw,ne,se,nw,se,sw,sw,nw,nw,nw,nw,nw,se,nw,ne,nw,nw,se,se,se,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,ne,n,nw,nw,ne,se,nw,nw,sw,s,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,se,n,n,sw,nw,nw,se,s,nw,n,nw,s,nw,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,sw,n,n,nw,ne,ne,n,nw,sw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,s,nw,nw,nw,nw,nw,nw,nw,n,nw,ne,n,nw,nw,nw,nw,nw,ne,ne,nw,nw,nw,nw,nw,sw,ne,nw,ne,s,nw,nw,sw,nw,nw,nw,nw,nw,nw,se,nw,nw,nw,nw,nw,nw,nw,se,n,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,s,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,sw,nw,nw,nw,nw,se,n,se,n,nw,nw,nw,nw,nw,nw,nw,nw,n,sw,nw,nw,s,s,n,n,nw,sw,nw,n,nw,s,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,nw,nw,n,n,nw,n,nw,se,nw,nw,nw,nw,s,nw,nw,nw,nw,se,n,nw,s,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,sw,n,nw,nw,ne,n,nw,ne,n,s,n,n,ne,n,nw,nw,ne,nw,nw,nw,n,sw,nw,sw,nw,n,s,nw,nw,nw,nw,n,nw,nw,nw,nw,sw,nw,nw,n,sw,nw,sw,nw,n,ne,nw,nw,sw,n,n,nw,nw,nw,sw,nw,n,nw,nw,nw,s,nw,nw,nw,nw,nw,n,nw,nw,nw,sw,nw,se,n,nw,nw,s,nw,n,nw,se,n,sw,n,nw,n,nw,nw,nw,nw,n,n,n,n,nw,sw,s,nw,nw,n,se,nw,n,nw,nw,nw,ne,sw,nw,se,nw,n,s,ne,s,nw,n,n,n,nw,nw,nw,n,nw,nw,nw,nw,n,n,nw,nw,n,sw,n,se,nw,nw,nw,n,nw,nw,ne,n,se,n,ne,n,n,se,n,n,n,nw,n,nw,n,nw,ne,nw,nw,nw,n,n,n,n,nw,se,n,sw,nw,nw,n,s,nw,n,nw,n,n,nw,n,nw,n,ne,nw,sw,nw,sw,nw,nw,nw,nw,ne,nw,nw,n,ne,sw,nw,nw,n,n,se,nw,n,sw,nw,nw,se,n,nw,n,ne,nw,nw,se,nw,ne,n,n,se,n,nw,nw,nw,nw,nw,n,nw,n,nw,nw,nw,n,n,nw,nw,ne,nw,nw,nw,n,n,nw,nw,s,se,nw,n,nw,n,n,ne,nw,nw,n,n,nw,sw,nw,nw,nw,nw,nw,nw,nw,s,n,n,n,n,n,nw,nw,nw,nw,n,n,nw,n,s,n,nw,nw,nw,nw,sw,ne,nw,nw,nw,nw,nw,nw,se,nw,n,n,nw,s,sw,nw,nw,n,n,nw,n,n,nw,n,nw,sw,n,n,nw,n,nw,ne,sw,nw,nw,nw,n,n,nw,s,s,nw,nw,nw,nw,nw,n,nw,n,n,s,nw,nw,n,nw,n,nw,se,n,n,nw,n,n,sw,s,nw,s,nw,nw,n,n,nw,nw,nw,nw,n,nw,sw,n,se,n,nw,nw,n,n,nw,n,n,nw,n,n,se,nw,sw,n,nw,nw,n,s,sw,s,n,n,nw,n,n,n,se,n,nw,nw,se,se,n,n,n,nw,nw,ne,n,n,n,n,n,sw,n,nw,n,s,nw,nw,n,ne,nw,se,nw,nw,n,nw,sw,n,n,n,nw,n,nw,nw,n,nw,n,n,nw,nw,n,n,nw,n,sw,n,n,n,se,ne,nw,nw,sw,nw,n,s,nw,nw,n,nw,n,nw,n,nw,n,nw,nw,nw,n,nw,n,nw,n,n,nw,n,nw,nw,n,nw,n,n,n,nw,n,sw,n,nw,n,nw,n,n,nw,nw,n,n,nw,n,nw,nw,sw,n,n,nw,nw,nw,n,n,n,n,n,nw,n,ne,nw,nw,n,ne,n,nw,nw,sw,se,n,n,n,sw,n,n,ne,n,ne,nw,nw,nw,n,n,n,ne,nw,n,n,nw,n,n,nw,n,n,n,n,nw,n,nw,sw,n,ne,n,nw,nw,n,nw,n,se,n,n,nw,n,n,n,nw,ne,s,nw,nw,nw,n,n,sw,n,sw,sw,n,n,n,n,n,n,sw,nw,n,n,n,nw,n,nw,n,n,se,n,ne,n,nw,n,nw,n,n,n,n,n,n,ne,se,n,nw,n,nw,n,nw,n,nw,nw,n,n,n,sw,se,nw,n,n,nw,ne,nw,n,nw,nw,nw,n,n,s,se,s,n,sw,sw,n,n,nw,ne,s,n,nw,n,nw,n,n,se,n,n,n,sw,n,n,n,n,n,nw,nw,n,nw,nw,n,n,nw,n,n,n,n,n,n,n,n,nw,n,ne,nw,n,nw,nw,n,s,se,nw,n,se,n,s,n,n,n,nw,sw,n,n,nw,n,nw,n,se,n,sw,nw,n,n,n,n,n,nw,s,nw,n,n,n,n,nw,n,n,nw,n,nw,n,n,nw,n,nw,n,n,s,n,s,n,nw,sw,ne,n,n,n,nw,n,n,n,n,n,n,s,n,s,n,nw,n,n,nw,n,n,s,n,n,sw,s,n,n,n,nw,n,sw,n,n,ne,n,n,n,n,n,n,n,sw,n,n,n,nw,n,n,n,n,n,n,n,n,n,n,nw,nw,n,n,ne,n,n,n,se,n,nw,s,sw,nw,n,n,sw,nw,se,n,n,nw,n,n,n,s,sw,n,ne,n,n,nw,n,n,n,s,ne,ne,s,sw,n,ne,n,n,n,n,n,se,n,n,n,n,n,n,n,n,n,n,n,n,sw,n,s,n,n,n,se,nw,nw,n,nw,n,se,sw,n,n,n,nw,sw,ne,nw,se,n,n,n,ne,n,nw,n,n,n,n,nw,n,n,n,n,n,n,sw,n,ne,n,nw,n,n,n,n,n,se,n,n,n,n,n,n,n,n,n,ne,n,n,n,n,nw,se,se,ne,n,n,n,nw,n,n,se,n,n,n,n,ne,n,se,ne,n,n,n,se,s,sw,n,n,n,n,n,s,n,n,s,n,n,n,n,s,n,sw,nw,n,n,s,n,n,n,ne,ne,n,ne,n,sw,n,se,n,n,n,nw,n,n,n,n,sw,nw,n,s,n,n,se,n,nw,n,n,n,n,n,n,se,n,n,n,n,n,se,n,n,n,n,s,n,n,n,n,se,se,n,n,s,n,n,n,nw,n,n,n,n,n,n,n,ne,n,ne,n,n,n,n,ne,n,n,n,n,se,n,n,n,n,n,ne,n,n,n,se,n,s,n,n,s,n,n,se,n,n,n,n,ne,n,s,n,n,ne,n,n,ne,nw,n,ne,n,ne,n,ne,n,n,s,n,sw,ne,s,n,n,n,n,se,n,ne,n,n,n,s,n,n,n,sw,n,n,n,n,n,n,n,n,nw,n,n,n,n,n,n,ne,ne,s,n,n,s,n,n,n,nw,nw,ne,n,sw,n,n,n,ne,se,n,sw,se,n,sw,n,n,nw,n,n,n,ne,n,n,n,n,n,n,s,nw,n,n,n,n,sw,n,n,n,n,n,n,sw,ne,n,n,n,nw,ne,n,n,n,sw,nw,ne,s,nw,n,n,n,n,n,n,ne,n,n,n,n,n,n,n,n,n,n,se,n,s,se,nw,n,n,n,n,s,n,n,n,ne,n,n,ne,n,ne,n,ne,ne,n,n,n,s,ne,n,ne,n,n,n,ne,se,n,n,n,ne,n,n,ne,n,n,n,s,n,ne,n,n,n,n,n,n,n,n,n,n,n,n,ne,n,n,n,n,ne,n,n,n,se,n,ne,n,s,n,n,ne,n,sw,n,se,n,s,n,ne,n,s,ne,s,n,n,se,n,ne,n,ne,n,ne,n,sw,n,n,s,ne,n,ne,ne,n,sw,n,n,s,ne,n,n,s,n,s,n,n,n,ne,n,s,ne,n,ne,n,n,n,s,n,n,ne,s,n,ne,se,ne,nw,n,n,n,nw,n,n,ne,sw,s,n,n,n,n,se,n,n,ne,ne,n,nw,n,ne,n,n,n,n,ne,n,s,n,sw,n,n,n,n,ne,n,n,n,n,s,sw,ne,n,n,n,n,n,ne,n,n,s,se,se,sw,n,n,n,n,ne,ne,n,ne,n,n,se,sw,n,ne,n,n,n,nw,ne,n,ne,n,ne,n,se,ne,ne,n,n,n,n,n,n,se,ne,nw,sw,n,nw,ne,n,n,ne,sw,ne,s,n,se,se,ne,s,n,sw,ne,n,n,n,ne,n,ne,n,ne,n,n,ne,ne,n,ne,ne,n,se,n,ne,ne,n,sw,ne,ne,ne,ne,n,n,n,ne,nw,ne,n,n,n,n,n,n,n,n,ne,ne,n,ne,n,ne,se,ne,n,ne,n,n,sw,sw,n,n,ne,n,n,ne,ne,s,n,ne,ne,ne,n,ne,ne,s,n,sw,s,nw,n,n,n,se,n,ne,n,se,ne,ne,ne,sw,ne,ne,n,ne,n,n,n,ne,nw,n,n,n,ne,n,nw,n,n,se,nw,n,ne,n,ne,n,ne,n,ne,nw,nw,n,ne,ne,sw,n,ne,ne,ne,ne,n,n,n,se,n,n,n,s,ne,ne,n,n,n,ne,n,n,n,nw,ne,ne,n,ne,n,n,ne,n,sw,n,ne,n,n,ne,n,n,ne,n,n,ne,ne,sw,ne,ne,ne,se,n,sw,n,ne,n,n,n,n,ne,s,n,ne,n,ne,n,ne,n,ne,se,ne,ne,n,ne,ne,ne,n,ne,ne,n,n,n,n,n,n,n,n,n,n,ne,se,n,n,n,ne,n,n,ne,ne,n,n,ne,ne,n,se,nw,se,n,sw,ne,ne,ne,ne,ne,ne,ne,n,n,ne,n,ne,n,ne,n,ne,n,s,s,ne,ne,se,n,n,sw,n,n,n,ne,ne,nw,n,n,n,ne,n,n,n,n,n,ne,ne,ne,ne,n,ne,ne,n,ne,ne,sw,n,n,n,nw,se,ne,ne,n,n,n,s,n,n,se,s,nw,ne,n,ne,ne,ne,ne,nw,s,n,se,sw,ne,ne,ne,n,ne,n,ne,sw,n,n,ne,ne,ne,se,s,s,ne,ne,ne,s,n,ne,n,ne,ne,ne,n,s,se,ne,n,n,se,n,ne,ne,n,ne,ne,n,ne,ne,n,n,n,nw,n,ne,n,ne,n,s,se,sw,ne,ne,n,n,ne,s,ne,ne,n,ne,ne,ne,ne,n,ne,ne,ne,ne,n,n,se,ne,s,ne,ne,ne,ne,ne,n,ne,ne,ne,n,n,ne,n,ne,ne,ne,ne,n,n,n,n,n,nw,ne,n,ne,s,n,ne,n,ne,n,ne,ne,nw,ne,sw,nw,ne,n,n,s,se,nw,ne,nw,ne,ne,n,n,ne,n,se,ne,n,ne,n,n,ne,n,s,ne,ne,n,se,ne,nw,ne,ne,sw,ne,ne,n,ne,ne,n,ne,s,ne,sw,n,n,ne,n,n,ne,ne,ne,s,n,n,n,n,nw,n,n,n,n,ne,ne,nw,ne,ne,n,ne,n,ne,n,ne,ne,ne,n,sw,ne,ne,ne,ne,ne,n,sw,ne,n,ne,ne,ne,n,ne,n,ne,n,s,s,n,ne,ne,n,ne,n,ne,n,ne,nw,ne,se,n,n,ne,n,n,ne,ne,n,ne,n,n,n,n,n,ne,ne,ne,n,ne,n,ne,ne,n,ne,ne,ne,ne,ne,n,n,ne,n,n,n,ne,ne,ne,ne,ne,sw,n,n,ne,n,ne,ne,nw,n,ne,n,ne,ne,n,sw,n,n,ne,ne,nw,ne,nw,ne,se,se,se,ne,ne,se,ne,sw,n,n,ne,ne,ne,ne,n,ne,ne,se,ne,ne,ne,ne,n,ne,ne,ne,n,s,ne,se,se,ne,ne,ne,n,ne,n,n,ne,n,nw,ne,ne,n,ne,se,sw,ne,ne,ne,n,ne,ne,n,ne,ne,sw,ne,ne,ne,ne,n,sw,n,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,n,se,n,ne,n,n,ne,ne,n,ne,ne,n,ne,n,ne,ne,n,ne,n,n,ne,ne,n,n,ne,sw,ne,nw,ne,n,ne,se,ne,ne,sw,ne,ne,ne,n,ne,ne,n,n,n,ne,nw,ne,n,ne,ne,ne,n,ne,n,sw,ne,s,se,ne,ne,sw,ne,ne,ne,ne,ne,se,ne,ne,n,ne,ne,ne,ne,ne,ne,n,n,n,ne,n,ne,ne,ne,n,n,ne,ne,nw,s,ne,ne,se,ne,n,ne,ne,ne,ne,ne,n,ne,ne,ne,nw,s,n,ne,ne,ne,n,ne,ne,se,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,s,ne,sw,ne,ne,ne,ne,nw,n,sw,ne,ne,ne,ne,sw,ne,nw,ne,n,n,n,ne,ne,n,ne,se,sw,sw,ne,n,ne,n,ne,ne,nw,ne,ne,se,ne,ne,sw,ne,se,ne,n,ne,ne,ne,sw,ne,ne,ne,ne,nw,ne,n,ne,ne,ne,n,ne,ne,ne,ne,se,ne,ne,n,ne,n,ne,ne,n,ne,n,sw,ne,ne,n,s,ne,ne,ne,ne,s,ne,ne,se,n,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,n,ne,ne,ne,n,n,s,ne,ne,sw,se,n,ne,ne,ne,ne,ne,n,ne,n,ne,ne,ne,ne,n,ne,ne,ne,ne,s,ne,nw,s,ne,se,se,ne,ne,ne,ne,sw,se,ne,ne,sw,se,ne,n,ne,n,ne,ne,n,sw,ne,ne,s,n,ne,ne,s,ne,s,n,ne,ne,ne,ne,n,n,ne,ne,s,se,ne,ne,ne,se,ne,ne,ne,sw,ne,sw,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,s,nw,ne,ne,n,ne,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,nw,ne,ne,ne,n,se,ne,ne,s,n,n,ne,n,ne,nw,ne,nw,ne,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,n,ne,ne,nw,ne,ne,sw,ne,ne,ne,n,ne,ne,ne,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,ne,ne,nw,ne,ne,ne,ne,ne,ne,ne,ne,ne,nw,ne,ne,ne,ne,ne,nw,ne,ne,n,n,sw,sw,sw,sw,se,s,sw,s,sw,se,s,sw,s,sw,sw,se,se,s,n,se,se,se,se,se,se,nw,se,se,ne,ne,se,ne,nw,nw,ne,ne,sw,ne,ne,ne,ne,se,se,ne,n,ne,n,n,n,ne,n,n,ne,n,n,n,n,nw,n,n,se,n,n,n,sw,se,n,n,se,se,n,nw,n,n,n,sw,n,nw,se,nw,nw,nw,se,n,n,s,nw,nw,nw,nw,nw,sw,nw,nw,se,nw,se,nw,n,nw,nw,sw,nw,nw,nw,nw,nw,nw,ne,nw,nw,nw,s,nw,nw,sw,sw,nw,sw,nw,nw,sw,nw,sw,nw,nw,nw,s,sw,sw,nw,sw,nw,s,sw,sw,ne,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,n,sw,sw,sw,s,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,se,nw,sw,sw,sw,sw,sw,s,s,sw,sw,s,sw,ne,sw,sw,sw,sw,s,nw,s,s,s,sw,sw,sw,nw,s,sw,s,sw,se,s,n,s,s,s,s,s,nw,s,s,s,s,se,se,s,s,s,nw,s,s,s,s,s,s,n,s,s,s,s,s,s,nw,s,s,s,se,s,se,nw,n,nw,se,n,s,n,sw,se,s,s,s,se,se,s,s,nw,se,s,n,s,se,s,s,sw,se,n,s,sw,s,se,s,s,se,se,se,s,s,se,s,se,se,se,se,se,se,se,s,s,s,s,n,s,s,se,n,nw,se,nw,sw,nw,se,nw,se,se,se,se,se,se,se,sw,se,s,se,se,nw,se,ne,se,se,se,s,se,se,se,se,se,sw,se,n,ne,se,ne,s,se,sw,se,se,se,se,nw,sw,se,se,n,ne,se,ne,se,se,ne,se,nw,se,se,se,se,se,se,se,nw,se,se,se,n,se,ne,ne,se,ne,se,se,se,ne,nw,se,se,se,n,sw,ne,s,ne,ne,se,nw,se,ne,nw,ne,se,ne,se,se,se,se,se,sw,ne,nw,se,sw,n,se,se,se,se,se,se,se,se,se,ne,sw,se,ne,ne,s,ne,se,se,se,se,nw,ne,ne,ne,ne,ne,ne,n,ne,s,se,se,ne,ne,ne,se,se,ne,ne,se,ne,ne,s,s,ne,ne,ne,ne,ne,se,se,n,ne,ne,ne,s,nw,sw,n,ne,ne,ne,ne,s,ne,s,ne,ne,ne,ne,ne,n,s,nw,ne,nw,n,sw,nw,se,ne,ne,nw,se,ne,ne,n,ne,ne,ne,ne,sw,se,n,n,ne,ne,ne,ne,n,ne,ne,n,n,ne,ne,sw,n,ne,ne,ne,ne,ne,ne,se,ne,nw,se,ne,sw,ne,ne,ne,ne,ne,n,ne,ne,n,n,ne,n,n,ne,n,se,n,sw,ne,ne,ne,ne,sw,ne,n,ne,ne,ne,ne,se,ne,ne,sw,ne,n,n,ne,ne,ne,n,ne,ne,ne,ne,n,ne,n,n,ne,n,ne,n,ne,sw,n,n,n,nw,ne,n,n,n,n,ne,n,ne,ne,n,sw,sw,n,nw,n,ne,n,se,s,n,ne,sw,n,ne,ne,sw,n,n,sw,nw,n,n,n,s,n,n,n,ne,n,se,ne,n,n,s,n,nw,ne,ne,n,se,n,n,n,n,n,n,n,n,n,n,ne,sw,n,nw,n,n,sw,n,sw,n,n,ne,n,n,n,n,n,n,n,n,ne,n,ne,s,ne,n,n,ne,se,n,n,n,n,n,n,n,n,s,n,n,s,n,sw,se,n,n,n,n,n,ne,n,n,ne,se,n,nw,n,n,ne,nw,n,n,ne,n,n,nw,se,n,n,n,n,n,n,n,n,n,n,nw,n,n,n,n,n,n,ne,n,n,s,n,n,n,nw,n,n,n,n,n,n,n,n,n,se,se,ne,n,se,n,n,n,n,n,n,n,n,n,nw,n,nw,n,nw,n,n,n,n,n,sw,n,nw,n,nw,n,n,se,nw,n,nw,n,s,nw,nw,n,ne,n,se,n,sw,nw,nw,nw,nw,nw,nw,se,n,n,n,nw,n,n,s,nw,s,nw,n,nw,nw,se,sw,n,n,n,n,ne,nw,n,nw,nw,ne,n,nw,sw,nw,nw,n,se,nw,se,nw,nw,n,n,n,nw,nw,n,n,n,nw,nw,n,ne,nw,n,ne,nw,nw,s,se,nw,nw,n,s,nw,n,n,n,n,nw,nw,n,n,se,nw,s,n,nw,nw,nw,nw,nw,nw,nw,sw,nw,nw,nw,sw,n,nw,nw,n,nw,s,nw,nw,se,n,n,n,ne,nw,ne,nw,nw,nw,nw,nw,n,nw,ne,n,nw,n,nw,se,n,n,nw,nw,n,nw,nw,nw,nw,se,n,s,ne,sw,n,s,nw,nw,nw,nw,nw,ne,ne,s,nw,se,nw,nw,n,nw,nw,nw,nw,nw,s,nw,nw,n,nw,nw,nw,nw,nw,ne,sw,nw,nw,nw,ne,nw,nw,nw,nw,nw,se,nw,nw,ne,nw,se,ne,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,se,nw,nw,nw,nw,nw,sw,ne,nw,nw,nw,nw,nw,nw,ne,nw,n,nw,nw,nw,n,nw,ne,nw,nw,nw,nw,n,nw,se,nw,nw,s,nw,ne,nw,nw,ne,ne,nw,ne,nw,ne,nw,nw,nw,nw,nw,nw,sw,nw,ne,sw,nw,sw,nw,n,nw,se,nw,nw,nw,nw,nw,nw,nw,sw,se,nw,n,sw,sw,n,nw,n,nw,s,nw,nw,nw,nw,nw,nw,nw,nw,sw,sw,nw,sw,nw,nw,se,se,nw,nw,n,s,s,nw,nw,nw,sw,nw,sw,ne,se,s,nw,s,nw,sw,nw,nw,nw,sw,nw,sw,sw,s,nw,nw,nw,nw,nw,sw,nw,ne,nw,nw,nw,se,nw,nw,n,sw,sw,sw,sw,nw,nw,nw,sw,nw,sw,sw,nw,nw,sw,sw,n,se,nw,nw,nw,s,se,nw,sw,s,se,se,se,sw,sw,sw,nw,sw,sw,sw,nw,nw,nw,sw,nw,n,se,sw,sw,s,sw,sw,sw,nw,nw,sw,n,nw,nw,sw,n,s,sw,sw,nw,sw,nw,sw,sw,nw,sw,sw,nw,nw,s,sw,nw,sw,nw,nw,sw,nw,sw,sw,nw,sw,se,sw,n,sw,se,nw,sw,nw,ne,nw,sw,s,nw,sw,sw,sw,n,sw,sw,nw,n,nw,sw,sw,s,sw,sw,nw,sw,nw,nw,sw,sw,nw,nw,nw,sw,sw,sw,sw,nw,sw,sw,ne,sw,sw,se,sw,sw,s,nw,sw,sw,sw,nw,sw,s,sw,sw,s,ne,sw,sw,nw,sw,sw,nw,nw,nw,sw,sw,nw,sw,sw,sw,sw,sw,n,nw,sw,sw,nw,ne,nw,n,sw,sw,sw,n,nw,sw,n,sw,sw,sw,sw,sw,sw,n,ne,nw,nw,nw,sw,sw,n,n,sw,sw,sw,sw,sw,sw,se,sw,sw,nw,sw,ne,sw,sw,ne,nw,sw,nw,sw,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,se,se,sw,sw,sw,sw,sw,se,sw,nw,se,nw,sw,n,nw,sw,ne,ne,sw,sw,sw,sw,sw,se,sw,n,sw,sw,n,sw,sw,sw,sw,sw,sw,sw,ne,sw,sw,se,sw,sw,sw,sw,sw,sw,se,s,s,sw,s,ne,sw,se,sw,sw,sw,sw,sw,ne,s,s,nw,sw,sw,sw,sw,sw,sw,s,n,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,se,s,sw,nw,sw,ne,sw,s,s,sw,sw,sw,sw,sw,sw,s,s,sw,sw,nw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,n,sw,s,s,s,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,ne,s,nw,s,s,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,s,s,se,se,s,se,sw,sw,nw,sw,sw,sw,sw,s,ne,sw,s,s,s,sw,sw,nw,n,s,s,sw,n,nw,s,s,sw,ne,sw,s,nw,sw,ne,s,s,sw,s,sw,sw,sw,sw,s,s,sw,sw,sw,nw,sw,n,s,sw,sw,sw,sw,s,s,nw,sw,s,nw,ne,sw,se,sw,s,sw,sw,ne,sw,s,sw,n,sw,s,se,se,sw,sw,ne,s,sw,sw,sw,sw,n,sw,sw,s,s,sw,nw,sw,ne,s,s,sw,sw,n,sw,ne,sw,se,sw,sw,s,s,s,sw,s,s,nw,n,sw,sw,ne,sw,s,ne,nw,s,se,s,sw,nw,s,n,s,sw,sw,nw,n,sw,sw,s,n,s,sw,n,s,s,s,s,s,s,sw,s,sw,s,s,s,sw,sw,n,sw,sw,s,sw,sw,sw,sw,sw,sw,s,sw,sw,s,se,s,sw,n,se,nw,sw,s,s,se,se,sw,sw,s,se,s,nw,n,s,sw,s,nw,se,sw,s,s,sw,s,sw,sw,s,sw,sw,s,s,se,n,nw,sw,sw,s,sw,sw,sw,s,s,s,sw,ne,s,s,se,sw,sw,sw,sw,n,s,s,s,sw,se,sw,n,s,sw,sw,nw,sw,s,s,sw,s,s,ne,s,s,s,s,sw,ne,sw,nw,s,sw,ne,sw,sw,ne,s,sw,nw,s,s,sw,s,s,s,s,s,nw,sw,s,se,s,s,s,n,s,sw,s,s,s,sw,s,nw,s,s,s,n,s,s,se,s,s,se,sw,ne,s,s,sw,se,s,s,s,se,s,sw,se,s,s,sw,se,s,s,s,s,nw,s,sw,sw,s,s,nw,s,ne,s,s,s,sw,s,s,sw,s,nw,sw,s,sw,sw,s,s,s,ne,sw,nw,s,s,s,s,s,s,s,sw,s,s,s,s,s,se,s,s,s,s,s,s,sw,s,sw,s,s,s,se,s,s,s,s,s,se,nw,n,se,s,s,s,s,s,s,nw,n,s,s,s,sw,s,s,s,s,n,s,s,nw,n,s,se,s,s,n,s,n,s,s,n,sw,s,s,s,nw,sw,se,ne,ne,s,s,s,ne,n,nw,s,se,sw,s,s,s,s,s,s,se,s,s,s,s,s,se,s,s,s,s,s,nw,s,s,s,s,n,s,nw,s,s,se,s,nw,s,s,s,s,s,nw,s,s,s,s,s,ne,s,nw,s,s,ne,s,ne,s,s,s,s,s,s,ne,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,se,s,s,ne,s,sw,s,nw,s,s,s,s,s,ne,s,se,s,s,s,s,s,s,s,s,ne,s,s,ne,s,s,s,n,s,s,n,s,s,s,s,s,n,n,s,s,s,ne,s,s,ne,s,se,n,s,s,s,n,se,s,s,s,s,s,s,s,s,s,s,se,s,s,s,n,s,s,ne,se,s,s,s,sw,se,n,s,se,s,s,ne,s,se,s,s,nw,nw,se,se,se,se,s,s,s,s,se,se,nw,se,se,sw,s,s,s,ne,s,nw,s,s,sw,se,s,se,se,s,s,n,s,s,ne,s,s,s,s,n,s,s,sw,s,se,nw,sw,s,n,s,s,ne,s,se,s,nw,s,s,nw,s,se,sw,s,se,s,se,ne,se,se,se,s,nw,s,nw,s,nw,se,n,se,se,se,s,s,s,s,se,s,nw,se,nw,s,se,sw,se,se,se,n,s,ne,se,s,s,se,s,s,ne,se,ne,sw,se,s,se,s,s,s,s,se,s,s,s,s,s,se,se,se,s,n,se,se,s,s,se,s,se,s,s,s,se,nw,se,se,s,se,se,s,ne,ne,se,s,ne,n,se,s,s,se,s,s,se,s,s,s,sw,se,s,s,se,sw,se,se,s,se,s,s,s,nw,s,s,s,se,se,se,s,s,s,s,sw,s,se,se,s,s,s,s,s,sw,sw,se,s,se,se,s,s,s,se,s,se,se,s,s,se,s,se,s,ne,ne,s,s,se,s,s,s,s,s,s,se,s,s,se,se,sw,s,ne,s,s,se,s,se,sw,se,n,s,s,s,se,s,s,s,se,s,se,s,ne,se,se,s,s,s,s,se,se,se,se,se,se,se,s,s,ne,nw,s,s,se,s,ne,s,s,se,se,s,n,s,s,se,nw,s,s,se,se,s,se,s,se,s,se,nw,se,ne,n,s,s,se,se,ne,se,nw,se,se,se,se,se,se,se,se,s,s,se,se,n,se,s,se,se,nw,s,sw,se,sw,n,se,s,s,se,s,ne,se,s,ne,se,se,s,s,s,se,nw,se,se,se,se,s,se,se,se,se,se,se,se,s,se,se,se,sw,se,n,se,se,sw,se,se,se,se,se,se,s,se,se,n,se,se,se,se,se,se,se,s,se,se,se,s,se,nw,s,s,se,se,s,se,se,s,se,se,s,n,se,se,se,se,se,se,se,s,s,se,se,se,s,se,s,s,n,nw,se,se,s,se,s,se,s,sw,se,se,nw,se,nw,s,n,s,se,s,s,se,se,se,nw,se,nw,nw,se,se,s,s,s,nw,se,n,ne,se,se,se,se,ne,se,se,se,s,se,sw,s,n,s,s,se,se,s,n,s,se,se,sw,se,se,se,s,se,sw,s,se,se,se,se,se,ne,se,se,se,se,se,se,s,se,se,se,se,se,se,se,n,se,se,ne,s,se,se,se,s,se,ne,se,se,se,se,se,se,se,s,se,se,se,se,se,se,se,se,sw,se,se,se,se,nw,s,se,se,nw,se,s,s,se,se,se,se,se,se,se,se,se,sw,se,se,n,nw,n,se,ne,se,n,se,nw,nw,se,ne,s,se,se,s,se,se,s,se,se,s,se,s,se,n,se,se,se,se,se,n,s,se,se,se,se,se,se,s,se,se,nw,ne,s,se,ne,se,se,se,n,se,se,se,s,se,se,se,se,se,se,n,se,se,s,se,se,s,s,se,se,se,se,se,n,ne,se,se,nw,se,se,se,se,se,se,se,se,se,se,se,se,s,n,se,s,s,s,se,n,ne,se,s,se,se,se,ne,ne,s,se,se,s,se,se,se,se'
    print("part1:", part1(input_data))
    print("part2:", part2(input_data))
