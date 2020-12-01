import itertools

import aoc_helper


def parse_raw(raw):
    return list(map(int, raw.split('\n')))


def part_one():
    a, b = next(filter(
        lambda x: sum(x) == 2020, itertools.combinations(data, 2)
    ))
    return a * b


def part_two():
    a, b, c = next(filter(
        lambda x: sum(x) == 2020, itertools.combinations(data, 3)
    ))
    return a * b * c


data = parse_raw(aoc_helper.day(1))

aoc_helper.submit(day=1, solv_func=part_one)
aoc_helper.submit(day=1, solv_func=part_two)
