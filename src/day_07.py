import aoc_helper

raw = aoc_helper.day(7)

def parse_raw():
    bags = {}
    for line in raw.split('\n'):
        container, inside = line.split('s contain ')
        inside_bags = {}
        for inside_part in inside[:-1].split(', '):
            if inside_part == 'no other bags':
                break
            number = int(inside_part[0])
            bag = inside_part[2:].rstrip('s')
            inside_bags[bag] = number
        bags[container] = inside_bags
    return bags

data = parse_raw()

def part_one():
    can_carry = ['shiny gold bag']
    old_can_carry = None
    while old_can_carry != can_carry:
        old_can_carry = list(can_carry)
        for bag in data:
            if bag in can_carry:
                continue
            for can_carry_bag in can_carry:
                if can_carry_bag in data[bag]:
                    can_carry.append(bag)
                    break
    print(can_carry)
    return len(set(can_carry)) - 1


def part_two(container_bag='shiny gold bag'):
    total = 1
    for bag, amount in data[container_bag].items():
        total += part_two(bag) * amount
    return total

aoc_helper.submit(day=7, solv_func=part_one)
aoc_helper.submit(day=7, solv_func=lambda: part_two() - 1)
