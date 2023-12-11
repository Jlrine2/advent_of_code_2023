from pathlib import Path

from aoc_utils import parse_lines, aoc_main

from collections import Counter

SAMPLE_INPUT_1 = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip("\n").split("\n")

SAMPLE_INPUT_2 = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip("\n").split("\n")
PART_1_SAMPLE_ANSWER = 6440
PART_2_SAMPLE_ANSWER = 5905
INPUT = parse_lines((Path(__file__).parent / "inputs.txt").absolute())


def get_tie_breaker_value(hand, cards):
    v = ''
    for card in hand:
        t = str(cards.index(card) + 2)
        if len(t) == 1:
            t = '0' + t
        v += t
    return int(v)


def handle_jokers(hand: str):
    print("JLRFOO")
    if 'J' not in hand:
        return hand
    if hand == "JJJJJ":
        return hand
    h1 = hand.replace('J', '')
    print(h1)
    m = Counter(h1).most_common()[0][0]
    print(m)
    n = len(hand) - len(h1)
    print(n)
    j = m * n
    return h1 + j


def get_hand_value(hand, cards, jokers=False):
    jhand = handle_jokers(hand) if jokers else hand
    print(jhand)
    c = sorted(Counter(jhand).values(), reverse=True)[:2]
    if c[0] == 5:
        print(f"{hand}: 5 OAK: {get_tie_breaker_value(hand, cards)}")
        return 70 ** 10 + get_tie_breaker_value(hand, cards)
    if c[0] == 4:
        print(f"{hand}: 4 OAK")
        return 60 ** 10 + get_tie_breaker_value(hand, cards)
    if c == [3, 2]:
        print(f"{hand}: Full House")
        return 50 ** 10 + get_tie_breaker_value(hand, cards)
    if c[0] == 3:
        print(f"{hand}: 3 OAK")
        return 40 ** 10 + get_tie_breaker_value(hand, cards)
    if c == [2, 2]:
        print(f"{hand}: 2 Pair")
        return 30 ** 10 + get_tie_breaker_value(hand, cards)
    if c[0] == 2:
        print(f"{hand}: Pair")
        return 20 ** 10 + get_tie_breaker_value(hand, cards)
    if len(Counter(hand).values()) == 5:
        print(f"{hand}: High Card")
        return 10 ** 10 + get_tie_breaker_value(hand, cards)
    print("nothing")


def part_1(lines):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    vbids = []
    for hand, bid in (line.split() for line in lines):
        value = get_hand_value(hand, cards)
        vbids.append((value, int(bid)))
    solution = 0
    for i, bid in enumerate(sorted(vbids)):
        v = bid[1] * (i + 1)
        solution += v
    return solution

def part_2(lines):
    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    vbids = []
    for hand, bid in (line.split() for line in lines):
        value = get_hand_value(hand, cards, jokers=True)
        vbids.append((value, int(bid)))
    solution = 0
    for i, bid in enumerate(sorted(vbids)):
        v = bid[1] * (i + 1)
        solution += v
    return solution


if __name__ == '__main__':
    aoc_main(__name__)
