import re
from pprint import pprint
from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
30373
25512
65332
33549
35390
""", 21),
]


def solve(input):
    rows = input.strip().split('\n')
    height = len(rows)
    width = len(rows[0])
    visible = set()

    watermark = ['.'] * height
    for col in range(0, width):
        for row in range(0, height):
            if rows[row][col] > watermark[row]:
                visible.add((row, col))
                watermark[row] = rows[row][col]
    watermark = ['.'] * height
    for col in range(width - 1, -1, -1):
        for row in range(0, height):
            if rows[row][col] > watermark[row]:
                visible.add((row, col))
                watermark[row] = rows[row][col]

    watermark = ['.'] * width
    for row in range(0, height):
        for col in range(0, width):
            if rows[row][col] > watermark[col]:
                visible.add((row, col))
                watermark[col] = rows[row][col]

    watermark = ['.'] * width
    for row in range(height - 1, - 1, -1):
        for col in range(0, width):
            if rows[row][col] > watermark[col]:
                visible.add((row, col))
                watermark[col] = rows[row][col]

    for row in range(0, height):
        for col in range(0, width):
            if (row, col) in visible:
                print('X', end='')
            else:
                print('.', end='')
        print('\n', end='')
    print(visible)
    return len(visible)


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
