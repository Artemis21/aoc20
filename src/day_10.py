import itertools

import aoc_helper


def parse_raw():
    return list(map(int, raw.split('\n')))


def part_one():
    adapters = list(sorted(data))
    adapters.append(adapters[-1] + 3)
    count_one = 0
    count_three = 0
    last = 0
    while adapters:
        this = adapters.pop(0)
        if this - last == 1:
            count_one += 1
        elif this - last == 3:
            count_three += 1
        elif this - last not in (1,2,3):
            raise ValueError(this, last)
        last = this
    return count_one * count_three


def part_two():
    adapters = list(sorted(data))
    adapters.append(adapters[-1] + 3)
    segments = [[0]]
    last = 0
    last_diff = 3
    while adapters:
        this = adapters.pop(0)
        if this - last == 3:
            if last_diff == 3:
                segments[-1] = [this]
            else:
                segments[-1].append(this)
                segments.append([this])
        else:
            segments[-1].append(this)
        last_diff = this - last
        last = this
    if len(segments[-1]) == 1:
        segments.pop(-1)
    possible_arrangements = 1
    for segment in segments:
        possible_this = 0
        possible_orderings = itertools.chain(*[itertools.combinations(
            segment[1:-1], this_len
        ) for this_len in range(len(segment) - 1)])
        for inner_segment in possible_orderings:
            full_segment = [*inner_segment, segment[-1]]
            last = segment[0]
            valid = True
            for adapter in full_segment:
                if adapter - last not in (1, 2, 3):
                    valid = False
                    break
                last = adapter
            if valid:
                possible_this += 1
        possible_arrangements *= possible_this
    return possible_arrangements


raw = aoc_helper.day(10)
data = parse_raw()

aoc_helper.submit(day=10, solv_func=part_one)
aoc_helper.submit(day=10, solv_func=part_two)
