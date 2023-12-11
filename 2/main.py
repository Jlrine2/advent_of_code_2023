from pathlib import Path

from aoc_utils import parse_lines, aoc_main

SAMPLE_INPUT_1 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 8
PART_2_SAMPLE_ANSWER = 2286
INPUT = parse_lines((Path(__file__).parent / "inputs.txt").absolute())


def part_1(lines):
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    games = set()
    count = 0
    errors = set()
    for line in lines:
        count += 1
        line = line.split(': ')[1]
        rounds = line.split(';')
        for _round in rounds:
            colors = _round.split(',')
            games.add(count)
            for color in colors:
                spl = color.strip(' ').split(' ')
                number = spl[0]
                name = spl[1]
                if cubes[name] < int(number):
                    errors.add(count)
        pass
    return sum(games.difference(errors))


def part_2(lines):
    solution = 0
    for line in lines:
        line = line.split(": ")[1]
        rounds = line.split(';')
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for _ROUND in rounds:
            colors = _ROUND.split(',')
            for color in colors:
                spl = color.strip(' ').split(' ')
                if spl[0]:
                    number = spl[0]
                    name = spl[1]
                    if cubes[name] < int(number):
                        cubes[name] = int(number)
        import numpy
        solution += numpy.prod(list(cubes.values()))
    return solution


if __name__ == '__main__':
    aoc_main(__name__)
