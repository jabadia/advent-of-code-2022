from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""", 13),
]

DIRECTION = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}


def do_step(head, tail, direction):
    head = head[0] + DIRECTION[direction][0], head[1] + DIRECTION[direction][1]
    dist = tail[0] - head[0], tail[1] - head[1]
    if abs(dist[0]) == 2 or abs(dist[1]) == 2:
        dist = dist[0] // abs(dist[0] or 1), dist[1] // abs(dist[1] or 1)
        tail = tail[0] - dist[0], tail[1] - dist[1]

    return head, tail


def print_world(visited, head, tail):
    print()
    world = visited | {head, tail}
    min_row = min(row for row, col in world)
    max_row = max(row for row, col in world)
    min_col = min(col for row, col in world)
    max_col = max(col for row, col in world)
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) == head:
                print('H', end='')
            elif (row, col) == tail:
                print('T', end='')
            elif (row, col) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()


def solve(input):
    head = tail = (0, 0)
    visited = {tail}
    for move in input.strip().split('\n'):
        direction, steps = move.split(' ')
        for i in range(int(steps)):
            head, tail = do_step(head, tail, direction)
            visited.add(tail)
            # print_world(visited, head, tail)
            pass

    return len(visited)


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
