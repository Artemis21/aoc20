import sqlite3
import re


def get_input():
    print('Please enter the puzzle input:')
    inp = []
    while (line := input('... ')):
        m = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        a, b, letter, password = m.groups()
        inp.append((int(a), int(b), letter, password))
    return inp


def store_input():
    cursor.execute(
        'CREATE TABLE entries ('
        '    a INTEGER, b INTEGER, letter STRING, password STRING);'
    )
    inp = get_input()
    cursor.executemany('INSERT INTO entries VALUES (?, ?, ?, ?);', inp)
    db.commit()


def part_one():
    cursor.execute(
        'SELECT COUNT(password) FROM entries '
        'WHERE password '
        'REGEXP "^([^" || letter || "]*" || letter || "){" || a || "," || b || "}[^" || letter || "]*$"'
    )
    return cursor.fetchone()[0]


def part_two():
    cursor.execute(
        'SELECT COUNT(password) FROM entries '
        'WHERE (password '
        'REGEXP "^.{" || CAST(a - 1 as VARCHAR) || "}" || letter || ".{" || CAST(b - a - 1 as VARCHAR) || "}[^" || letter || "]") '
        '<> (password '
        'REGEXP "^.{" || CAST(a - 1 as VARCHAR) || "}[^" || letter || "].{" || CAST(b - a - 1 as VARCHAR) || "}" || letter)'
    )
    return cursor.fetchone()[0]


def regexp(expr, item):
    return re.search(expr, item) is not None


db = sqlite3.connect(':memory:')
db.create_function('REGEXP', 2, regexp)
cursor = db.cursor()

store_input()
print(part_one())
print(part_two())
