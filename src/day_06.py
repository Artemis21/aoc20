import aoc_helper


def parse_raw():
    groups = raw.split('\n\n')
    parsed = []
    for group in groups:
        parsed.append(group)
    return parsed


def part_one():
    return sum(len(set(i.replace('\n', ''))) for i in data)


def part_two():
    total = 0
    for group in data:
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if all(i in ans for ans in group.split('\n')):
                total += 1
    return total


raw = aoc_helper.day(6)
data = parse_raw()

aoc_helper.submit(day=6, solv_func=part_one)
aoc_helper.submit(day=6, solv_func=part_two)
