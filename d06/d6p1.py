from itertools import zip_longest
import re

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    TestCase('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    TestCase('nppdvjthqldpwncqszvftbrmjlhg', 6),
    TestCase('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    TestCase('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)
]


def solve(input):
    for i in range(len(input) - 4):
        if len(set(input[i:i + 4])) == 4:
            return i + 4
    return None


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
