from pathlib import Path

from aoc_utils import get_lines, aoc_main

from matplotlib.path import Path as mPath

SAMPLE_INPUT_1 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 8
PART_2_SAMPLE_ANSWER = 4
INPUT = get_lines((Path(__file__).parent / "inputs.txt").absolute())


class Node:
    def __init__(self, shape, x, y):
        adjustments = {
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(0, 1), (-1, 0)],
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(0, 1), (1, 0)],
            'S': None
        }
        self.shape = shape
        self.directions = adjustments[shape]
        self.x = x
        self.y = y

    def next(self, prev, map):
        nodes = []
        for a, b in self.directions:
            try:
                n = map[(self.x + a)][(self.y + b)]
                nodes.append(n)
            except IndexError:
                nodes.append(None)
        if nodes[0] == prev or nodes[0] is None:
            return nodes[1]
        return nodes[0]

    def __repr__(self):
        return f"{self.shape}: {self.x},{self.y}"


def part_1(lines):
    map = []
    start = None
    for i, line in enumerate(lines):
        nodes = []
        for j, n in enumerate(line):
            if n in '|-LJ7FS':
                _n = Node(n, i, j)
                nodes.append(_n)
                if n == 'S':
                    start = _n
            else:
                nodes.append(None)
        map.append(nodes)
    for (x, y), range in [((1, 0), '|LJ'), ((-1, 0), '|7F'), ((0, 1), '-J7'), ((0, -1), '-FL')]:
        x, y = start.x + x, start.y + y
        if map[x][y] and map[x][y].shape in range:
            prev = start
            current = map[x][y]
            count = 1
            while current.shape != "S":
                count += 1
                tmp = current.next(prev, map)
                prev = current
                current = tmp
            return int(count / 2)


def part_2(lines):
    map = []
    start = None
    for i, line in enumerate(lines):
        nodes = []
        for j, n in enumerate(line):
            if n in '|-LJ7FS':
                _n = Node(n, i, j)
                nodes.append(_n)
                if n == 'S':
                    start = _n
            else:
                nodes.append(None)
        map.append(nodes)
    path = None
    verticies = [(start.x, start.y)]
    for (x, y), range in [((1, 0), '|LJ'), ((-1, 0), '|7F'), ((0, 1), '-J7'), ((0, -1), '-FL')]:
        x, y = start.x + x, start.y + y
        if map[x][y] and map[x][y].shape in range:
            prev = start
            current = map[x][y]
            count = 1
            while current.shape != "S":
                verticies.append((current.x, current.y))
                count += 1
                tmp = current.next(prev, map)
                prev = current
                current = tmp
            verticies.append((start.x, start.y))
            break
    path = mPath(verticies)
    solution = 0
    for i, row in enumerate(map):
        for j, _ in enumerate(row):
            if (i, j) not in verticies:
                if path.contains_point((i, j)):
                    solution += 1
    return solution


if __name__ == '__main__':
    aoc_main(__name__)
