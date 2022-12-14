from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
A Y
B X
C Z
""", 15),
]


SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

OUTCOMES = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},  # rock
    'B': {'X': 0, 'Y': 3, 'Z': 6},  # paper
    'C': {'X': 6, 'Y': 0, 'Z': 3},  # scissors
}


def solve(input):
    rounds = input.strip().split('\n')
    score = 0
    for round in rounds:
        their_selection, my_selection = round.split(' ')
        score += SCORES[my_selection] + OUTCOMES[their_selection][my_selection]
    return score


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
