import re

from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""", 10605)
]


class Monkey:
    def __init__(self, definition):
        self.id = -1
        self.items = []
        self.test_divisor = 0
        self.operation = ''
        self.target_monkeys = {
            True: None,
            False: None
        }
        self.items_inspected = 0
        self.parse(definition)

    def parse(self, definition):
        lines = definition.split('\n')
        matches = re.match(r'Monkey (\d+):', lines[0].strip())
        self.id = int(matches.group(1))
        matches = re.match(r'Starting items: (.+)', lines[1].strip())
        self.items = [int(item) for item in matches.group(1).split(', ')]
        matches = re.match(r'Operation: (.+)', lines[2].strip())
        self.operation = matches.group(1)
        matches = re.match(r'Test: divisible by (\d+)', lines[3].strip())
        self.test_divisor = int(matches.group(1))
        matches = re.match(r'If true: throw to monkey (\d+)', lines[4].strip())
        self.target_monkeys[True] = int(matches.group(1))
        matches = re.match(r'If false: throw to monkey (\d+)', lines[5].strip())
        self.target_monkeys[False] = int(matches.group(1))

    def __repr__(self):
        return f'Monkey {self.id}, items: {self.items}, operation: {self.operation}, ' \
               f'test divisible by {self.test_divisor}, targets: {self.target_monkeys}'

    def inspect(self, item, other_monkeys):
        self.items_inspected += 1
        self.items.remove(item)
        old = item
        item = eval(self.operation.split(' = ')[1])
        item = item // 3
        is_divisible = item % self.test_divisor == 0
        other_monkeys[self.target_monkeys[is_divisible]].items.append(item)


def solve(input):
    monkeys = [Monkey(definition) for definition in input.strip().split('\n\n')]

    for round in range(20):
        for monkey in monkeys:
            for item in list(monkey.items):
                monkey.inspect(item, monkeys)

    monkeys = sorted(monkeys, key=lambda monkey: monkey.items_inspected, reverse=True)
    return monkeys[0].items_inspected * monkeys[1].items_inspected


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
