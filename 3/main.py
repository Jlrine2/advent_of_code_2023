from pathlib import Path

from aoc_utils import parse_lines, aoc_main

SAMPLE_INPUT_1 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 4361
PART_2_SAMPLE_ANSWER = 467835
INPUT = parse_lines((Path(__file__).parent / "inputs.txt").absolute())


def part_1(lines):
    solution = 0
    schematic = []
    for line in lines:
        r = ["."]
        r.extend(list(line))
        r.extend(".")
        schematic.append(r)
    schematic.append(["." for i in range(len(schematic[0]))])
    for i, row in enumerate(schematic):
        current_number = {
            "value": 0,
            "start": -1,
            "end": -1
        }
        for j, column in enumerate(row):
            if column.isdigit():
                current_number["value"] *= 10
                current_number["value"] += int(column)
                if current_number["start"] == -1:
                    current_number["start"] = j
            else:
                if current_number["value"] == 0:
                    continue
                current_number["end"] = j
                if any(not c.isdigit() and c != "." for c in
                       schematic[i - 1][current_number["start"] - 1:current_number["end"] + 1]
                       ) or any(not c.isdigit() and c != "." for c in
                                schematic[i + 1][current_number["start"] - 1:current_number["end"] + 1]
                                ) or any(not c.isdigit() and c != "." for c in
                                         schematic[i][current_number["start"] - 1:current_number["end"] + 1]):
                    solution += current_number["value"]
                current_number = {
                    "value": 0,
                    "start": -1,
                    "end": -1
                }
    return solution


def part_2(lines):
    solution = 0
    schematic = []
    for line in lines:
        r = ["."]
        r.extend(list(line))
        r.extend(".")
        schematic.append(r)
    schematic.append(["." for i in range(len(schematic[0]))])
    for i, row in enumerate(schematic):
        for j, column in enumerate(row):
            if column == "*":
                adj_numbers = []
                top_numbers = []
                current_number = {
                    "value": 0,
                    "start": -1,
                    "end": -1
                }
                for k, c in enumerate(schematic[i - 1]):
                    if c.isdigit():
                        current_number["value"] *= 10
                        current_number["value"] += int(c)
                        if current_number["start"] == -1:
                            current_number["start"] = k
                    else:
                        if current_number["value"] == 0:
                            continue
                        current_number["end"] = k
                        top_numbers.append(current_number)
                        current_number = {
                            "value": 0,
                            "start": -1,
                            "end": -1
                        }
                for k, c in enumerate(schematic[i + 1]):
                    if c.isdigit():
                        current_number["value"] *= 10
                        current_number["value"] += int(c)
                        if current_number["start"] == -1:
                            current_number["start"] = k
                    else:
                        if current_number["value"] == 0:
                            continue
                        current_number["end"] = k
                        top_numbers.append(current_number)
                        current_number = {
                            "value": 0,
                            "start": -1,
                            "end": -1
                        }
                for k, c in enumerate(schematic[i]):
                    if c.isdigit():
                        current_number["value"] *= 10
                        current_number["value"] += int(c)
                        if current_number["start"] == -1:
                            current_number["start"] = k
                    else:
                        if current_number["value"] == 0:
                            continue
                        current_number["end"] = k
                        top_numbers.append(current_number)
                        current_number = {
                            "value": 0,
                            "start": -1,
                            "end": -1
                        }
                for n in top_numbers:
                    if j in range(n["start"]-1, n["end"]+1):
                        adj_numbers.append(n)
                if len(adj_numbers) == 2:
                    solution += adj_numbers[0]["value"] * adj_numbers[1]["value"]
    return solution


if __name__ == '__main__':
    aoc_main(__name__)
