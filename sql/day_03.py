import sqlite3
import math


def get_input():
    print('Please enter the puzzle input:')
    inp = []
    y = 0
    while (line := input('... ')):
        for x, char in enumerate(line):
            inp.append((x, y, char))
        y += 1
    return inp


def store_input():
    cursor.execute('CREATE TABLE squares (x INTEGER, y INTEGER, tile CHARACTER(1));')
    inp = get_input()
    cursor.executemany('INSERT INTO squares VALUES (?, ?, ?);', inp)
    db.commit()


def part_one():
    cursor.execute(
        'SELECT COUNT(y) FROM squares '
        'WHERE x = (3 * y) % (SELECT COUNT(x) FROM squares WHERE y = 0) '
        'AND tile = "#"'
    )
    return cursor.fetchone()[0]


def part_two():
    cursor.execute('CREATE TABLE slopes (slope REAL);')
    cursor.execute('INSERT INTO slopes VALUES (1), (3), (5), (7), (0.5);')
    cursor.execute(
        'SELECT CAST(EXP(SUM(LOG(trees))) as INTEGER) FROM ('
        '    SELECT COUNT(y) trees '
        '    FROM squares CROSS JOIN slopes '
        '    WHERE tile = "#" '
        '    AND CAST(slope * y AS INTEGER) = slope * y '
        '    AND x = (slope * y) % (SELECT COUNT(x) FROM squares WHERE y = 0) '
        '    GROUP BY slope'
        ')'
    )
    return cursor.fetchone()[0]


db = sqlite3.connect(':memory:')
# Most DBs have LOG and EXP functions, but SQLite doesn't.
db.create_function('LOG', 1, math.log)
db.create_function('EXP', 1, math.exp)
cursor = db.cursor()

store_input()
print(part_one())
print(part_two())
