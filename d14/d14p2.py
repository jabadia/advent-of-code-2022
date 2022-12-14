from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9    
""", 93)
]


def draw_world(world, rocks):
    minx = min(x for x, y in world)
    maxx = max(x for x, y in world)
    miny = min(y for x, y in world)
    maxy = max(y for x, y in world)
    print()
    for y in range(miny, maxy + 1):
        print(f'{y:3} ', end='')
        for x in range(minx, maxx + 1):
            if (x, y) in rocks:
                print('#', end='')
            elif (x, y) in world:
                print('o', end='')
            else:
                print('.', end='')
        print()


def move(pos, world, floor):
    x, y = pos
    if (x, y + 1) not in world and y != floor:
        return x, y + 1
    elif (x - 1, y + 1) not in world and y != floor:
        return x - 1, y + 1
    elif (x + 1, y + 1) not in world and y != floor:
        return x + 1, y + 1
    else:
        return False


def solve(input):
    world = set()
    for path in input.strip().split('\n'):
        points = path.split(' -> ')
        for p0, p1 in zip(points[:-1], points[1:]):
            x0, y0 = map(int, p0.split(','))
            x1, y1 = map(int, p1.split(','))
            delta_x, delta_y = (x1 - x0) // (abs(x1 - x0) or 1), (y1 - y0) // (abs(y1 - y0) or 1)
            x, y = x0, y0
            while x != x1 or y != y1:
                world.add((x, y))
                x += delta_x
                y += delta_y
            world.add((x, y))

    rocks = world.copy()
    floor = max(y for x, y in world) + 1
    source = (500, 0)

    units = 0
    while True:
        pos = source
        while True:
            new_pos = move(pos, world, floor)
            if not new_pos:
                world.add(pos)
                units += 1
                if pos == source:
                    draw_world(world, rocks)
                    return units
                break
            pos = new_pos


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    submit_answer(answer)
