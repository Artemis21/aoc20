import sqlite3


def get_input():
    print('Please enter the puzzle input:')
    raw = ''
    while (line := input('... ')):
        raw += '\n' + line
    return raw[1:]


def parse_raw(raw):
    outer_bags = []
    inner_bags = []
    for line in raw.split('\n'):
        container, inside = line.split(' bags contain ')
        for inside_part in inside[:-1].split(', '):
            if inside_part == 'no other bags':
                break
            number = int(inside_part[0])
            bag = inside_part[2:].rstrip('s').rstrip(' bag')
            inner_bags.append((container, bag, number))
        outer_bags.append((container,))
    return outer_bags, inner_bags


def store_input():
    outer_bags, inner_bags = parse_raw(get_input())
    cursor.execute('CREATE TABLE outer_bags (colour VARCHAR)')
    cursor.execute(
        'CREATE TABLE inner_bags (container VARCHAR, colour VARCHAR, number INTEGER)'
    )
    cursor.executemany('INSERT INTO outer_bags VALUES (?)', outer_bags)
    cursor.executemany('INSERT INTO inner_bags VALUES (?, ?, ?)', inner_bags)
    db.commit()


def part_one():
    cursor.execute(
        'WITH RECURSIVE can_carry (colour) AS ('
        '    SELECT "shiny gold" UNION ALL'
        '    SELECT outer_bags.colour FROM outer_bags'
        '        INNER JOIN inner_bags ON inner_bags.container = outer_bags.colour '
        '        INNER JOIN can_carry ON can_carry.colour = inner_bags.colour'
        ') SELECT DISTINCT colour FROM can_carry'
    )
    return cursor.fetchall()


db = sqlite3.connect(':memory:')
db.set_trace_callback(print)
cursor = db.cursor()

store_input()
print(part_one())
