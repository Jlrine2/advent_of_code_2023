from pathlib import Path

from aoc_utils import get_lines, aoc_main, get_text

SAMPLE_INPUT_1 = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip("\n")

SAMPLE_INPUT_2 = SAMPLE_INPUT_1
PART_1_SAMPLE_ANSWER = 35
PART_2_SAMPLE_ANSWER = 46
INPUT = get_text((Path(__file__).parent / "inputs.txt").absolute())


def part_1(text):
    parts = text.split('\n\n')
    seeds = parts[0].split()[1:]
    path = [part.split('\n')[1:] for part in parts[1:]]
    locations = []
    for seed in seeds:
        cur = int(seed)
        for stop in path:
            for row in stop:
                dest_range, source_range, size = (int(i) for i in row.split())
                if cur in range(source_range, source_range + size):
                    cur = cur - (source_range-dest_range)
                    break
        locations.append(cur)
    solution = min(locations)
    return solution


def part_2(text):
    parts = text.split('\n\n')
    seeds_parts = parts[0].split()[1:]
    seed_ranges = []
    for i, _ in enumerate(seeds_parts):
        j = i*2
        if j >= len(seeds_parts):
            break
        seed_ranges.append(range(
                    int(seeds_parts[j]),
                    int(seeds_parts[j]) + int(seeds_parts[j+1]),
                )
        )
    for mapping in parts[1:]:
        ranges = mapping.splitlines()[1:]
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]
        valid_ranges = []

        for r in seed_ranges:
            for dest, source in ranges:
                difference = dest.start - source.start
                if r.stop <= source.start or source.stop <= r.start:
                    continue
                spl = range(max(r.start, source.start), min(r.stop, source.stop))
                r1 = range(r.start, spl.start)
                r2 = range(spl.stop, r.stop)
                if r1:
                    seed_ranges.append(r1)
                if r2:
                    seed_ranges.append(r2)
                valid_ranges.append(range(spl.start + difference, spl.stop + difference))
                break
            else:
                valid_ranges.append(r)

        seed_ranges = valid_ranges
    return min(x.start for x in seed_ranges)


if __name__ == '__main__':
    aoc_main(__name__)
