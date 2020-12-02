import re
from collections import namedtuple

import aoc_helper


Entry = namedtuple('Entry', ['a', 'b', 'letter', 'password'])


def parse_raw():
    lines = []
    for line in raw.split('\n'):
        m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        a, b, letter, password = m.groups()
        lines.append(Entry(int(a), int(b), letter, password))
    return lines


def part_one():
    return sum(
        entry.a <= entry.password.count(entry.letter) <= entry.b
        for entry in data
    )


def part_two():
    return sum(
        (entry.password[entry.a - 1] == entry.letter)
         ^ (entry.password[entry.b - 1] == entry.letter)
        for entry in data
    )


raw = aoc_helper.day(2)
data = parse_raw()

aoc_helper.submit(day=2, solv_func=part_one)
aoc_helper.submit(day=2, solv_func=part_two)
