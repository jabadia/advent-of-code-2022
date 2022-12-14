import re
from pprint import pprint
from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
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


def find_visible(world, row, col, delta_row, delta_col):
    i, j = row + delta_row, col + delta_col
    visible = 0
    while world[i][j] < world[row][col]:
        visible += 1
        i += delta_row
        j += delta_col
    if world[i][j] != 'Z':
        visible += 1
    return visible


def scenic_score(world, row, col):
    up = find_visible(world, row, col, -1, 0)
    down = find_visible(world, row, col, 1, 0)
    left = find_visible(world, row, col, 0, -1)
    right = find_visible(world, row, col, 0, 1)

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
        for row in range(1, height - 1)
        for col in range(1, width - 1)
    )


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
