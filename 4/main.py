from pathlib import Path

from aoc_utils import get_lines, aoc_main

SAMPLE_INPUT_1 = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 13
PART_2_SAMPLE_ANSWER = 30
INPUT = get_lines((Path(__file__).parent / "inputs.txt").absolute())


def part_1(lines):
    solution = 0
    for line in lines:
        parts = line.split()
        spl = parts.index('|')
        winning_numbers = parts[1:spl]
        card_numbers = parts[spl:]
        card_value = 0
        for number in card_numbers:
            if number in winning_numbers:
                if not card_value:
                    card_value = 1
                    continue
                card_value *= 2
        solution += card_value
    return solution


def part_2(lines):
    solution = 0
    num_copies = [1 for _ in lines]
    for i, line in enumerate(lines):
        parts = line.split()
        spl = parts.index('|')
        winning_numbers = parts[1:spl]
        card_numbers = parts[spl:]
        card_value = 0
        wins = 0
        for number in card_numbers:
            if number in winning_numbers:
                wins += 1
                num_copies[i+wins] += num_copies[i]
    return sum(num_copies)


if __name__ == '__main__':
    aoc_main(__name__)
