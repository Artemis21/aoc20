import sqlite3


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
    cursor.execute(
        'CREATE TABLE chars (idx INTEGER, row INTEGER, char VARCHAR(1));'
    )
    inp = get_input()
    cursor.executemany('INSERT INTO chars VALUES (?, ?, ?);', inp)
    db.commit()


def part_one():
    cursor.execute(
        'CREATE TABLE seats (id INTEGER)'
    )
    cursor.execute(
        'INSERT INTO seats (id) SELECT '
        'SUM((chars.char = "B" OR chars.char = "R") * (1 << 9 - chars.idx)) '
        'FROM chars GROUP BY chars.row'
    )
    cursor.execute('SELECT id FROM seats ORDER BY id DESC LIMIT 1')
    return cursor.fetchone()[0]


def part_two():
    cursor.execute(
        'SELECT id + 1 FROM seats WHERE ('
        '    SELECT seats_a.id FROM seats AS seats_a '
        '    WHERE seats_a.id = seats.id + 1 '
        ') IS NULL AND ( '
        '    SELECT seats_b.id FROM seats AS seats_b '
        '    WHERE seats_b.id = seats.id + 2 '
        ') IS NOT NULL;'
    )
    return cursor.fetchone()[0]


db = sqlite3.connect(':memory:')
cursor = db.cursor()

store_input()
print(part_one())
print(part_two())
