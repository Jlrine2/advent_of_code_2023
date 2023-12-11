from pathlib import Path

from aoc_utils import parse_lines, aoc_main

SAMPLE_INPUT_1 = """
a
b
c
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
d
e
f
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 1
PART_2_SAMPLE_ANSWER = 2
INPUT = parse_lines((Path(__file__).parent / "inputs.txt").absolute())


def part_1(lines):
    solution = 0
    return solution


def part_2(lines):
    solution = 0
    return solution


if __name__ == '__main__':
    aoc_main(__name__)
