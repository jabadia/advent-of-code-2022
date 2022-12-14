from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
A Y
B X
C Z
""", 12),
]


def solve(input):
    rounds = input.strip().split('\n')
    score = 0
    for round in rounds:
        their_selection, desired_result = round.split(' ')

        their_selection = ord(their_selection) - ord('A')
        desired_result = ord(desired_result) - ord('X')
        score += ((their_selection + desired_result + 2) % 3 + 1) + desired_result * 3
    return score


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
