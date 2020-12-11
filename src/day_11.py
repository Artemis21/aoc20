import aoc_helper
import time

raw = aoc_helper.day(11)

def parse_raw():
    return [list(i) for i in raw.split('\n')]

data = parse_raw()

def part_one():
    old = [list(i) for i in data]
    while True:
        new = [list(i) for i in old]
        for y, row in enumerate(old):
            for x, cell in enumerate(row):
                occupied_surrounding = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if not (dx or dy):
                            continue
                        sx = x + dx
                        sy = y + dy
                        if sx < 0 or sy < 0 or sx >= len(row) or sy >= len(data):
                            continue
                        if old[sy][sx] == '#':
                            occupied_surrounding += 1
                if cell == 'L' and occupied_surrounding == 0:
                    new[y][x] = '#'
                elif cell == '#' and occupied_surrounding >= 4:
                    new[y][x] = 'L'
        if new == old:
            break
        old = new
    return str(new).count('#')


def part_two():
    old = [list(i) for i in data]
    while True:
        new = [list(i) for i in old]
        for y, row in enumerate(old):
            for x, cell in enumerate(row):
                occupied_surrounding = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if not (dx or dy):
                            continue
                        sx = x + dx
                        sy = y + dy
                        while len(row) > sx >= 0 and len(data) > sy >= 0:
                            if old[sy][sx] == '#':
                                occupied_surrounding += 1
                            if old[sy][sx] != '.':
                                break
                            sx += dx
                            sy += dy
                if cell == 'L' and occupied_surrounding == 0:
                    new[y][x] = '#'
                elif cell == '#' and occupied_surrounding >= 5:
                    new[y][x] = 'L'
               # print(occupied_surrounding)
        if new == old:
            break
        old = new
    return str(new).count('#')


# aoc_helper.submit(day=11, solv_func=part_one)
aoc_helper.submit(day=11, solv_func=part_two)
