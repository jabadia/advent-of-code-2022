from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""", 29)
]


def neighbours(v, height, width):
    for delta in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        n = v[0] + delta[0], v[1] + delta[1]
        if 0 <= n[0] < height and 0 <= n[1] < width:
            yield n


def solve(input):
    world = input.strip().split('\n')
    for i, row in enumerate(world):
        if 'S' in row:
            world[i] = world[i].replace('S', 'a')
        if 'E' in row:
            start = (i, row.index('E'))
            world[i] = world[i].replace('E', 'z')

    height = len(world)
    width = len(world[0])

    visited = {start}
    queue = [(start, 0)]
    while queue:
        current, path_len = queue.pop(0)
        for neighbour in neighbours(current, height, width):
            if neighbour in visited:
                continue
            my_height = ord(world[current[0]][current[1]])
            neighbour_height = ord(world[neighbour[0]][neighbour[1]])
            if neighbour_height >= my_height - 1:
                if world[neighbour[0]][neighbour[1]] == 'a':
                    return path_len + 1
                queue.append((neighbour, path_len + 1))
                visited.add(neighbour)

    return None


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
