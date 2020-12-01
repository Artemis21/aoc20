import sqlite3


def get_input():
    print('Please enter the puzzle input:')
    inp = []
    while (line := input('... ')):
        inp.append(int(line))
    return inp


def store_input():
    cursor.execute('CREATE TABLE entries (value INTEGER);')
    inp = get_input()
    cursor.executemany('INSERT INTO entries VALUES (?);', ((i,) for i in inp))
    db.commit()


def part_one():
    cursor.execute(
        'SELECT a.value * b.value FROM (entries as a, entries as b) '
        'WHERE a.value + b.value = 2020 LIMIT 1'
    )
    return cursor.fetchone()[0]


def part_two():
    cursor.execute(
        'SELECT a.value * b.value * c.value '
        'FROM (entries as a, entries as b, entries as c) '
        'WHERE a.value + b.value + c.value = 2020 LIMIT 1'
    )
    return cursor.fetchone()[0]


db = sqlite3.connect(':memory:')
cursor = db.cursor()

store_input()
print(part_one())
print(part_two())
