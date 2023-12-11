from pathlib import Path
from pprint import pprint

from aoc_utils import parse_lines, aoc_main

SAMPLE_INPUT_1 = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 374
PART_2_SAMPLE_ANSWER = 82000210
INPUT = parse_lines((Path(__file__).parent / "inputs.txt").absolute())


def expand(map):
    rows = []
    for i, row in enumerate(map):
        if all(a == '.' for a in row):
            rows.append(i)
    cols = []
    for i, col in enumerate(zip(*map)):
        if all(a == '.' for a in col):
            cols.append(i)
    return rows, cols


def part_1(lines):
    map = []
    for line in lines:
        row = list(line)
        map.append(row)
    erows, ecols = expand(map)
    galexy_locations = []
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col == "#":
                galexy_locations.append((i, j))
    from itertools import combinations
    pairs = list(combinations(galexy_locations, 2))
    solution = 0
    for pair in pairs:
        d = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        for row in erows:
            if pair[0][0] < row < pair[1][0] or pair[0][0] > row > pair[1][0]:
                d += 1
        for col in ecols:
            if pair[0][1] < col < pair[1][1] or pair[0][1] > col > pair[1][1]:
                d += 1
        solution += d
    return solution


def part_2(lines):
    map = []
    for line in lines:
        row = list(line)
        map.append(row)
    erows, ecols = expand(map)
    galexy_locations = []
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col == "#":
                galexy_locations.append((i, j))
    from itertools import combinations
    pairs = list(combinations(galexy_locations, 2))
    solution = 0
    for pair in pairs:
        d = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        for row in erows:
            if pair[0][0] < row < pair[1][0] or pair[0][0] > row > pair[1][0]:
                d += 1_000_000-1
        for col in ecols:
            if pair[0][1] < col < pair[1][1] or pair[0][1] > col > pair[1][1]:
                d += 1_000_000-1
        solution += d
    return solution


if __name__ == '__main__':
    aoc_main(__name__)
