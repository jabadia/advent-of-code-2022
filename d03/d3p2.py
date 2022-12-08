from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""", 70),
]


def prio(ch):
    return ord(ch) - ord('a') + 1 if 'a' <= ch <= 'z' else ord(ch) - ord('A') + 27


def solve(input):
    total = 0
    rucksacks = input.strip().split('\n')
    for r1, r2, r3 in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3]):
        common = (set(r1) & set(r2) & set(r3)).pop()
        total += prio(common)
    return total


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
