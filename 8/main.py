from pathlib import Path

from aoc_utils import get_lines, aoc_main

SAMPLE_INPUT_1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 2
PART_2_SAMPLE_ANSWER = 6
INPUT = get_lines((Path(__file__).parent / "inputs.txt").absolute())


def part_1(lines):
    directions = lines[0]
    map = {}
    for line in lines[2:]:
        parts = line.split()
        node, left, right = parts[0], parts[2][1:-1], parts[3][:-1]
        map[node] = (left, right)
    node = 'AAA'
    steps = 0
    while True:
        for direction in directions:
            steps += 1
            if direction == "L":
                node = map[node][0]
            if direction == "R":
                node = map[node][1]
            if node == "ZZZ":
                return steps


def get_steps(directions, map, node):
    steps = 0
    while True:
        for direction in directions:
            steps += 1
            if direction == "L":
                node = map[node][0]
            if direction == "R":
                node = map[node][1]
            if node.endswith("Z"):
                return steps


def part_2(lines):
    directions = lines[0]
    map = {}
    for line in lines[2:]:
        parts = line.split()
        node, left, right = parts[0], parts[2][1:-1], parts[3][:-1]
        map[node] = (left, right)
    start_nodes = [node for node in map.keys() if node.endswith('A')]

    node_steps = []
    for node in start_nodes:
        node_steps.append(get_steps(directions, map, node))
    print(node_steps)
    import numpy
    arr = numpy.array(node_steps, 'int64')
    return numpy.lcm.reduce(arr)


if __name__ == '__main__':
    aoc_main(__name__)
