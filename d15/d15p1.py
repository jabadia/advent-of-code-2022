import re

from utils.fetch_input import fetch_input
from utils.submit_answer import submit_answer
from utils.test_case import TestCase
from utils.timing import timing

TEST_CASES = [
    TestCase(("""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3    
""", 10), 26)
]


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


@timing
def solve(input):
    if isinstance(input, tuple):
        input, row_y = input
    else:
        row_y = 2000000

    sensors = {}
    beacons = set()
    for line in input.strip().split('\n'):
        matches = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        sensor = tuple(map(int, (matches.group(1), matches.group(2))))
        beacon = tuple(map(int, (matches.group(3), matches.group(4))))
        sensor_dist = dist(sensor, beacon)
        sensors[sensor] = sensor_dist
        beacons.add(beacon)

    row = set()
    for sensor, sensor_dist in sensors.items():
        projection = sensor[0], row_y
        covered = sensor_dist - dist(sensor, projection)
        if covered > 0:
            for x in range(sensor[0] - covered, sensor[0] + covered + 1):
                row.add(x)

    row -= set(x for x, y in beacons if y == row_y)
    row -= set(x for x, y in sensors.keys() if y == row_y)

    return len(row)


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        assert case.check(result)

    answer = solve(input)
    print(answer)
    assert answer == 5256611
    # submit_answer(answer)
