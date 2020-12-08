import aoc_helper


def parse_raw():
    ops = []
    for line in raw.split('\n'):
        op, raw_num = line.split()
        ops.append((op, int(raw_num)))
    return ops


def part_one():
    already_executed = []
    index = 0
    acc = 0
    while index not in already_executed:
        print(index, len(data))
        op, arg = data[index]
        already_executed.append(index)
        if op == 'nop':
            index += 1
        elif op == 'acc':
            index += 1
            acc += arg
        elif op == 'jmp':
            index += arg
    return acc


def part_two():
    for change_index, op_and_arg in enumerate(data):
        if op_and_arg[0] == 'nop':
            program = list(data)
            program[change_index] = ('jmp', op_and_arg[1])
        elif op_and_arg[0] == 'jmp':
            program = list(data)
            program[change_index] = ('nop', op_and_arg[1])
        else:
            continue
        print(change_index)
        already_executed = []
        index = 0
        acc = 0
        while index not in already_executed:
            try:
                op, arg = program[index]
            except IndexError:
                return acc
            already_executed.append(index)
            if op == 'nop':
                index += 1
            elif op == 'acc':
                index += 1
                acc += arg
            elif op == 'jmp':
                index += arg


raw = aoc_helper.day(8)
data = parse_raw()
aoc_helper.submit(day=8, solv_func=part_one)
aoc_helper.submit(day=8, solv_func=part_two)
