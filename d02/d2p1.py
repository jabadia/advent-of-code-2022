from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
A Y
B X
C Z
""", 15),
]


def solve(input):
    rounds = input.strip().split('\n')
    score = 0
    for round in rounds:
        their_selection, my_selection = round.split(' ')
        their_selection = ord(their_selection) - ord('A')
        my_selection = ord(my_selection) - ord('X')
        score += (my_selection + 1) + (my_selection - their_selection) % 3 * 3
    return score


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
