from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

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
""", 24000),
]


def solve(input):
    elves_calories = input.strip().split('\n\n')
    return max(
        sum(int(calories) for calories in elf_calories.split('\n'))
        for elf_calories in elves_calories
    )


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
