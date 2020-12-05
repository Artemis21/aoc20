import aoc_helper


def parse_raw():
    ids = []
    for line in raw.split('\n'):
        as_binary = (line.replace('B', '1')
                         .replace('F', '0')
                         .replace('R', '1')
                         .replace('L', '0'))
        ids.append(int(as_binary, base=2))
    return ids


def part_one():
    return max(data)


def part_two():
    prev = None
    for sid in sorted(data):
        if prev and prev + 1 != sid:
            return prev + 1
        prev = sid


raw = aoc_helper.day(5)
data = parse_raw()

aoc_helper.submit(day=5, solv_func=part_one)
aoc_helper.submit(day=5, solv_func=part_two)
