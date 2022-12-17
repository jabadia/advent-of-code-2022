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
""", 20), 56000011)
]


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_covered(pos, sensors):
    for sensor, sensor_dist in sensors.items():
        if sensor_dist >= dist(sensor, pos):
            return True

    return False


@timing
def solve(input):
    if isinstance(input, tuple):
        input, size = input
    else:
        size = 4000000

    sensors = {}
    beacons = set()
    for line in input.strip().split('\n'):
        matches = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        sensor = tuple(map(int, (matches.group(1), matches.group(2))))
        beacon = tuple(map(int, (matches.group(3), matches.group(4))))
        sensor_dist = dist(sensor, beacon)
        sensors[sensor] = sensor_dist
        beacons.add(beacon)

    # if there is only one, it must be at the edge of some sensor coverage?
    for sensor, sensor_dist in sensors.items():
        sensor_dist += 1
        for dy in range(-sensor_dist, sensor_dist + 1):
            dx0 = - (sensor_dist - abs(dy))
            dx1 = + (sensor_dist - abs(dy))

            x0 = sensor[0] + dx0
            x1 = sensor[0] + dx1
            y = sensor[1] + dy

            if y < 0 or y >= size:
                continue

            if x0 >= 0 and not is_covered((x0, y), sensors):
                return x0 * 4000000 + y

            if x1 <= size and not is_covered((x1, y), sensors):
                return x1 * 4000000 + y


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    answer = solve(input)
    print(answer)
    # submit_answer(answer)
