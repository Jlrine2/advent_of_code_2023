from pathlib import Path
from aoc_utils import get_lines, aoc_main

SAMPLE_INPUT_1 = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 114
PART_2_SAMPLE_ANSWER = 2
INPUT = get_lines((Path(__file__).parent / "inputs.txt").absolute())


def recursive_solver(numbers):
    if all(i == 0 for i in numbers):
        return 0
    new = [numbers[i+1] - numbers[i] for i in range(0, len(numbers) - 1)]
    return numbers[-1] + recursive_solver(new)


def part_1(lines):
    solution = 0
    for line in lines:
        numbers = [int(i) for i in line.split()]
        solution += recursive_solver(numbers)
    return solution


def part_2(lines):
    solution = 0
    for line in lines:
        numbers = [int(i) for i in reversed(line.split())]
        solution += recursive_solver(numbers)
    return solution

if __name__ == '__main__':
    aoc_main(__name__)
