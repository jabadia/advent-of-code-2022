from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""", 157),
]


def prio(ch):
    return ord(ch) - ord('a') + 1 if 'a' <= ch <= 'z' else ord(ch) - ord('A') + 27


def solve(input):
    total = 0
    for rucksack in input.strip().split('\n'):
        first, second = set(rucksack[:len(rucksack) // 2]), set(rucksack[len(rucksack) // 2:])
        common = (first & second).pop()
        total += prio(common)
    return total


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
