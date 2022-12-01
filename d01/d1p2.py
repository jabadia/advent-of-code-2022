from utils.test_case import TestCase
from d1_input import INPUT

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
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
