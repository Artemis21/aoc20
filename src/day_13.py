import aoc_helper

raw = aoc_helper.day(13)
print(raw)

def parse_raw():
    raw_mins, raw_buses = raw.split('\n')
    buses = []
    for raw_bus in raw_buses.split(','):
        if raw_bus == 'x':
            buses.append(None)
        else:
            buses.append(int(raw_bus))
    return int(raw_mins), buses

data = parse_raw()

def part_one():
    min_time, buses = data
    soonest_bus = min((bus for bus in buses if bus), key=lambda bus: bus - (min_time % bus))
    print(soonest_bus, min_time, min_time % soonest_bus)
    return (soonest_bus - (min_time % soonest_bus)) * soonest_bus

def part_two():
    _, buses = data
    buses = list(sorted((i for i in enumerate(buses) if i[1]), key=lambda x: -x[1]))
    first, step = buses[0]
    first = (step - first) % step
    for idx, bus in buses[1:]:
        value = first
        while value % bus != (bus - idx) % bus:
            value += step
        first = value
        step *= bus
    return '{:f}'.format(first).split('.')[0]

aoc_helper.submit(day=13, solv_func=part_one)
aoc_helper.submit(day=13, solv_func=part_two)
