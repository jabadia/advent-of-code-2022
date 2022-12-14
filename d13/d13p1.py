from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""", 13)
]


def compare(first, second):
    if isinstance(first, int) and isinstance(second, int):
        return first - second
    else:
        if isinstance(first, int) != isinstance(second, int):
            if isinstance(first, int):
                first = [first]
            else:
                second = [second]
        # both are lists now
        for item1, item2 in zip(first, second):
            cmp = compare(item1, item2)
            if cmp == 0:
                continue
            return cmp
        return len(first) - len(second)


def solve(input):
    result = 0
    for index, pair in enumerate(input.strip().split('\n\n')):
        first, second = pair.split('\n')
        first = eval(first)
        second = eval(second)
        # first, second = fix_types(first, second)
        if compare(first, second) < 0:
            result += (index + 1)

    return result


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
