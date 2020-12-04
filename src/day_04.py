import aoc_helper
import math, itertools


raw = aoc_helper.day(4)


def parse_raw():
    passports = [{}]
    for line in raw.split('\n'):
        if not line:
            passports.append({})
        else:
            part = line.split(' ')
            parsed = {}
            for p in part:
                name, val = p.split(':')
                parsed[name] = val
            passports[-1].update(parsed)
    return passports


def part_one():
    total = 0
    for passport in data:
        valid = True
        for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if field not in passport:
                valid = False
                break
        if valid:
            total += 1
    return total


def part_two():
    total = 0
    lengths = {
        'byr': 4,
        'iyr': 4,
        'eyr': 4,
        'hcl': 7,
        'pid': 9
    }
    ranges = {
        'byr': (2002, 1920),
        'iyr': (2020, 2010),
        'eyr': (2030, 2020)
    }
    for passport in data:
        valid = True
        for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if field not in passport:
                valid = False
            if valid and field in lengths and len(passport[field]) != lengths[field]:
                valid = False
            if valid and field in ranges:
                value = int(passport[field])
                if value < ranges[field][0] or value > ranges[field][1]:
                    valid = False
        if not valid:
            continue
        if (height := passport['hgt']).endswith('cm'):
            h = int(height[:-2])
            if h < 150 or h > 193:
                continue
        elif height.endswith('in'):
            h = int(height[:-2])
            if h < 59 or h > 76:
                continue
        else:
            continue
        if not passport['hcl'].startswith('#'):
            continue
        hcl_valid = True
        for d in passport['hcl'][1:]:
            if d not in '0123456789abcdef':
                hcl_valid = False
                break
        if not hcl_valid:
            continue
        if passport['ecl'] not in (
                'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        total += 1
    return total


data = parse_raw()
aoc_helper.submit(day=4, solv_func=part_one)
aoc_helper.submit(day=4, solv_func=part_two)
