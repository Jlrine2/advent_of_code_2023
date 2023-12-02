from pathlib import Path

from aoc_utils import get_lines, aoc_main

SAMPLE_INPUT_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 142
PART_2_SAMPLE_ANSWER = 281
INPUT = get_lines((Path(__file__).parent / "inputs.txt").absolute())


def part_1(lines):
    solution = 0
    for line in lines:
        nums = ''.join(c for c in line if c.isdigit())
        if nums:
            number = int(nums[0] + nums[-1])
            solution += number
    return solution


def part_2(lines):
    import re
    number_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    solution = 0
    for line in lines:
        matches = re.findall(
            r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))",
            line,
        )
        number = 0
        if matches[0].isdigit():
            number += 10 * int(matches[0])
        else:
            number += 10 * int(number_map[matches[0]])
        if matches[-1].isdigit():
            number += int(matches[-1])
        else:
            number += int(number_map[matches[-1]])
        solution += number
    return solution


if __name__ == '__main__':
    aoc_main(__name__)
