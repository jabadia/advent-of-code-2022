from itertools import zip_longest
import re

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    TestCase('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    TestCase('nppdvjthqldpwncqszvftbrmjlhg', 23),
    TestCase('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    TestCase('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
]


def solve(input):
    for i in range(len(input) - 14):
        if len(set(input[i:i + 14])) == 14:
            return i + 14
    return None


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
