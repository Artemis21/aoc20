import math

import aoc_helper

raw = aoc_helper.day(12)

def parse_raw():
    moves = []
    for line in raw.split('\n'):
        moves.append((line[0], int(line[1:])))
    return moves

data = parse_raw()

def part_one():
    x = y = angle = 0
    for action, value in data:
        if action == 'N':
            y += value
        elif action == 'E':
            x += value
        elif action == 'S':
            y -= value
        elif action == 'W':
            x -= value
        elif action == 'L':
            angle -= value
        elif action == 'R':
            angle += value
        elif action == 'F':
            x += value * math.cos(math.radians(angle))
            y -= value * math.sin(math.radians(angle))
    return round(abs(x) + abs(y))

def part_two():
    x_ship = y_ship = 0
    x_waypoint = 10
    y_waypoint = 1
    for action, value in data:
        if action == 'N':
            y_waypoint += value
        elif action == 'E':
            x_waypoint += value
        elif action == 'S':
            y_waypoint -= value
        elif action == 'W':
            x_waypoint -= value
        elif action == 'L':
            angle = math.atan2(y_waypoint, x_waypoint)
            angle += math.radians(value)
            distance = (x_waypoint ** 2 + y_waypoint ** 2) ** 0.5
            x_waypoint = distance * math.cos(angle)
            y_waypoint = distance * math.sin(angle)
        elif action == 'R':
            angle = math.atan2(y_waypoint, x_waypoint)
            angle -= math.radians(value)
            distance = (x_waypoint ** 2 + y_waypoint ** 2) ** 0.5
            x_waypoint = distance * math.cos(angle)
            y_waypoint = distance * math.sin(angle)
        elif action == 'F':
            x_ship += x_waypoint * value
            y_ship += y_waypoint * value
    return round(abs(x_ship) + abs(y_ship))

# aoc_helper.submit(day=12, solv_func=part_one)
aoc_helper.submit(day=12, solv_func=part_two)
