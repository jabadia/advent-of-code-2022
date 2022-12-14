from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""", 4),
]


def overlaps(r0, r1, p0, p1):
    return p0 <= r1 and r0 <= p1


def solve(input):
    count = 0
    for pair in input.strip().split('\n'):
        elf1, elf2 = pair.split(',')
        r0, r1 = map(int, elf1.split('-'))
        p0, p1 = map(int, elf2.split('-'))
        if overlaps(r0, r1, p0, p1):
            count += 1
    return count


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
