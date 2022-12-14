from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase
import functools

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
""", 140)
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
    packets = input.strip().split('\n')
    packets = [eval(packet) for packet in packets if packet] + [[[2]], [[6]]]
    packets = sorted(packets, key=functools.cmp_to_key(compare))
    marker1 = 1 + packets.index([[2]])
    marker2 = 1 + packets.index([[6]])
    return marker1 * marker2


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
