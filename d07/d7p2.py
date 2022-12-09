import re
from pprint import pprint
from utils.fetch_input import fetch_input
from utils.test_case import TestCase

TEST_CASES = [
    TestCase("""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""", 24933642),
]


def dirsize(dir):
    if '__totalsize__' in dir:
        return dir['__totalsize__']
    total_size = dir['__ownsize__']
    for subdir_name, subdir in dir.items():
        if subdir_name in ('..', '__ownsize__', '__totalsize__'):
            continue
        total_size += dirsize(subdir)
    dir['__totalsize__'] = total_size
    return total_size


def find_sizes(dir, candidates):
    candidates.append(dirsize(dir))
    for subdir_name, subdir in dir.items():
        if subdir_name in ('..', '__ownsize__', '__totalsize__'):
            continue
        find_sizes(subdir, candidates)


def solve(input):
    disk = {
        '__ownsize__': 0,
    }
    pwd = disk
    for line in input.strip().split('\n'):
        line = line.strip()
        if line[0] == '$':
            if line == '$ cd /':
                pwd = disk
            elif line == '$ cd ..':
                pwd = pwd['..']
            elif line.startswith('$ cd'):
                newdir = line[5:]
                # noinspection PyTypeChecker
                pwd[newdir] = {
                    '..': pwd,
                    '__ownsize__': 0,
                }
                pwd = pwd[newdir]
            continue
        if line.startswith('dir'):
            continue
        matches = re.match(r'(\d+) (\w+)', line)
        size, file = matches.groups()
        size = int(size)
        pwd['__ownsize__'] += size

    total_space = 70000000
    required_space = 30000000
    used_space = dirsize(disk)
    needed_space = used_space - total_space + required_space

    candidates = []
    find_sizes(disk, candidates=candidates)
    for candidate in sorted(candidates):
        if candidate >= needed_space:
            return candidate


if __name__ == '__main__':
    input = fetch_input()
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(input))
