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
""", 1),
    TestCase("""
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""", 36),
]

DIRECTION = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}


def do_step(knots, direction):
    knots[0] = knots[0][0] + DIRECTION[direction][0], knots[0][1] + DIRECTION[direction][1]
    for i in range(1, 10):
        dist = knots[i][0] - knots[i-1][0], knots[i][1] - knots[i-1][1]
        if abs(dist[0]) == 2 or abs(dist[1]) == 2:
            dist = dist[0] // abs(dist[0] or 1), dist[1] // abs(dist[1] or 1)
            knots[i] = knots[i][0] - dist[0], knots[i][1] - dist[1]

    return knots


def print_world(visited, knots):
    print()
    world = visited | set(knots)
    min_row = min(row for row, col in world)
    max_row = max(row for row, col in world)
    min_col = min(col for row, col in world)
    max_col = max(col for row, col in world)
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            try:
                knot_index = knots.index((row, col))
                print('H' if 0 == knot_index else knot_index, end='')
            except ValueError:
                if (row, col) in visited:
                    print('#', end='')
                else:
                    print('.', end='')
        print()


def solve(input):
    knots = [(0, 0)] * 10
    visited = {knots[9]}
    for move in input.strip().split('\n'):
        direction, steps = move.split(' ')
        for i in range(int(steps)):
            knots = do_step(knots, direction)
            visited.add(knots[9])
            # print_world(visited, knots)
            pass

    return len(visited)


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
