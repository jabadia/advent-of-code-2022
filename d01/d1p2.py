import logging

from utils.test_case import TestCase
from utils.fetch_input import fetch_input

TEST_CASES = [
    TestCase("""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""", 45000),
]


def solve(input):
    elves_calories = input.strip().split('\n\n')
    return sum(
        sorted(
            (
                sum(int(calories) for calories in elf_calories.split('\n'))
                for elf_calories in elves_calories
            ),
            reverse=True
        )[:3]
    )


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
