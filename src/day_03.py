import aoc_helper


def parse_raw():
    return list(raw.split('\n'))


def part_one():
    x, y, count = 0, 0, 0
    while y < len(data):
        if data[y][x] == '#':
            count += 1
        x += 3
        x %= len(data[0])
        y += 1
    return count


def part_two():
    answer = 1
    for (dx, dy) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        x, y, count = 0, 0, 0
        while y < len(data):
            if data[y][x] == '#':
                count += 1
            x += dx
            x %= len(data[0])
            y += dy
        answer *= count
    return answer


raw = aoc_helper.day(3)
data = parse_raw()

aoc_helper.submit(day=3, solv_func=part_one)
aoc_helper.submit(day=3, solv_func=part_two)
