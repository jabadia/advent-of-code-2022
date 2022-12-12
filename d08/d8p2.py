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
""", 8),
]


def scenic_score(world, row, col):
    height = len(world)
    width = len(world[0])

    j = row - 1
    up = 0
    while world[j][col] < world[row][col]:
        up += 1
        j -= 1
    if world[j][col] != 'Z':
        up += 1

    j = row + 1
    down = 0
    while world[j][col] < world[row][col]:
        down += 1
        j += 1
    if world[j][col] != 'Z':
        down += 1

    i = col - 1
    left = 0
    while world[row][i] < world[row][col]:
        left += 1
        i -= 1
    if world[row][i] != 'Z':
        left += 1

    i = col + 1
    right = 0
    while world[row][i] < world[row][col]:
        right += 1
        i += 1
    if world[row][i] != 'Z':
        right += 1

    return up * down * left * right


def solve(input):
    world = input.strip().split('\n')
    height = len(world) + 2
    width = len(world[0]) + 2
    world = ['Z' * width] + [
        'Z' + row + 'Z' for row in world
    ] + ['Z' * width]

    return max(
        scenic_score(world, row, col)
        for row in range(1, height-1)
        for col in range(1, width-1)
    )


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
