import sqlite3


def get_input():
    print('Please enter the puzzle input:')
    inp = []
    y = 0
    while (line := input('... ')) != 'EOF':
        for x, char in enumerate(line):
            inp.append((x, y, char))
        y += 1
    return inp


def store_input():
    cursor.execute(
        'CREATE TABLE chars (idx INTEGER, row INTEGER, char VARCHAR)'
    )
    inp = get_input()
    cursor.executemany('INSERT INTO chars VALUES (?, ?, ?);', inp)
    cursor.execute(
        'INSERT INTO chars SELECT 0, search_chars.row + 1, "SPLIT" '
        'FROM chars AS search_chars WHERE search_chars.idx = 0 ('
        '    SELECT chars_a.char FROM chars AS chars_a'
        '    WHERE chars_a.row = search_chars.row + 1'
        ') IS NULL AND ('
        '    SELECT chars_b.char FROM chars AS chars_b'
        '    WHERE chars_b.row = search_chars.row + 2'
        ') IS NOT NULL'
    )
    cursor.execute(
        'CREATE TABLE answers ('
        '    group_no INTEGER, person INTEGER, answer VARCHAR'
        ')'
    )
    cursor.execute(
        'INSERT INTO answers SELECT IFNULL(('
        '    SELECT search_chars.row FROM chars AS search_chars WHERE'
        '    search_chars.char = "SPLIT" AND search_chars.row < chars.row'
        '    ORDER BY search_chars.row DESC LIMIT 1'
        '), 0), chars.row, chars.char FROM chars WHERE chars.char != "SPLIT"'
    )
    db.commit()


def part_one():
    cursor.execute(
        'SELECT SUM(total) FROM ('
        'SELECT COUNT(DISTINCT answer) total FROM answers GROUP BY group_no)'
    )
    return cursor.fetchone()[0]


def part_two():
    cursor.execute(
        'SELECT COUNT(DISTINCT answer || group_no) FROM answers WHERE ('
        '    SELECT COUNT(check_answers.answer) FROM answers AS check_answers'
        '    WHERE check_answers.group_no = answers.group_no'
        '    AND check_answers.answer = answers.answer'
        ') = ('
        '    SELECT COUNT(DISTINCT check_answers.person)'
        '    FROM answers AS check_answers'
        '    WHERE check_answers.group_no = answers.group_no'
        ')'
    )
    return cursor.fetchone()[0]


db = sqlite3.connect(':memory:')
cursor = db.cursor()

store_input()
print(part_one())
print(part_two())
