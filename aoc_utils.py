import sys
import time
from pathlib import Path


def parse_lines(file: Path) -> list[str]:
    lines = Path(file).read_text().strip("\n").split('\n')
    return lines


def get_text(file: Path) -> str:
    text = Path(file).read_text().strip("\n")
    return text


def aoc_main(module_name):
    module = sys.modules[module_name]
    if (answer_1 := module.part_1(module.SAMPLE_INPUT_1)) == module.PART_1_SAMPLE_ANSWER:
        start = time.time()
        ans = module.part_1(module.INPUT)
        end = time.time()
        print(f"Part_1: ✅ - Answer: {ans} - Time: {end - start}")
    else:
        print(f"Part_1: ❌ - Expecting {module.PART_1_SAMPLE_ANSWER}, got {answer_1}")

    if (answer_2 := module.part_2(module.SAMPLE_INPUT_2)) == module.PART_2_SAMPLE_ANSWER:
        start = time.time()
        ans = module.part_2(module.INPUT)
        end = time.time()
        print(f"Part_2: ✅ - Answer: Answer: {ans} - Time: {end - start}")
    else:
        print(f"Part_2: ❌ - Expecting {module.PART_2_SAMPLE_ANSWER}, got {answer_2}")
