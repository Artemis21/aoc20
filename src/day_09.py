import aoc_helper


def parse_raw():
    return list(map(int, raw.split('\n')))


def part_one():
    components = data[:25]
    to_parse = data[25:]
    while to_parse:
        valid = False
        for a in components:
            for b in components:
                if a != b and a + b == to_parse[0]:
                    valid = True
                    break
        if not valid:
            return to_parse[0]
        components.pop(0)
        components.append(to_parse.pop(0))


def part_two():
    target = part_one()
    for start in range(len(data) - 1):
        for end in range(start + 2, len(data) + 1):
            if sum(data[start:end]) == target:
                return min(data[start:end]) + max(data[start:end])


raw = aoc_helper.day(9)
data = parse_raw()

aoc_helper.submit(day=9, solv_func=part_one)
aoc_helper.submit(day=9, solv_func=part_two)
