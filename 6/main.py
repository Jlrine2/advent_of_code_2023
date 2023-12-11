from pathlib import Path

from aoc_utils import parse_lines, aoc_main

SAMPLE_INPUT_1 = """
Time:      7  15   30
Distance:  9  40  200
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
Time:      7  15   30
Distance:  9  40  200
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 288
PART_2_SAMPLE_ANSWER = 71503
INPUT = parse_lines((Path(__file__).parent / "inputs.txt").absolute())


def part_1(lines):
    times = map(int, lines[0].split()[1:])
    distances = list(map(int, lines[1].split()[1:]))
    wins = []
    for i, t in enumerate(times):
        win = 0
        for j in range(1, t):
            if ((t-j)*j) > distances[i]:
                win += 1
        wins.append(win)
    import numpy
    solution = numpy.prod(wins)
    return solution


def part_2(lines):
    time = int(lines[0].split(":")[1].replace(' ', ''))
    distance = int(lines[1].split(":")[1].replace(' ', ''))
    win = 0
    for j in range(1, time):
        if ((time - j) * j) > distance:
            win += 1
    return win


if __name__ == '__main__':
    aoc_main(__name__)
