from itertools import zip_longest
import re

from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""", 'MCD'),
]


def solve(input):
    stacks, moves = input.strip('\n').split('\n\n')
    stacks = zip_longest(*stacks.split('\n'), fillvalue=' ')
    stacks = [list(reversed(stack)) for stack in stacks if stack[-1] in '0123456789']
    stacks = {
        stack[0]: [crate for crate in stack[1:] if crate != ' ']
        for stack in stacks
    }
    for move in moves.split('\n'):
        matches = re.match(r'move (\d+) from (\d+) to (\d+)', move)
        count, source, target = matches.groups()
        count = int(count)
        stacks[target].extend(stacks[source][-count:])
        stacks[source] = stacks[source][:-count]
    return ''.join([stack.pop() for stack in stacks.values()])


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
