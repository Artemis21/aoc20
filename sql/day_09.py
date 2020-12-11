import sqlite3


def get_input():
    print('Please enter the puzzle input:')
    inp = []
    while (line := input('... ')):
        inp.append(int(line))
    return inp


def store_input():
    cursor.execute('CREATE TABLE numbers (idx INTEGER, value INTEGER)')
    inp = get_input()
    cursor.executemany('INSERT INTO numbers VALUES (?, ?);', enumerate(inp))
    db.commit()


def part_one():
    cursor.execute(
        'SELECT value FROM numbers WHERE ('
        '   SELECT numbers_a.value FROM (numbers AS numbers_a, numbers AS numbers_b)'
        '   WHERE numbers_a.value + numbers_b.value = numbers.value'
        '   AND numbers_a.value != numbers_b.value'
        '   AND numbers_a.idx BETWEEN numbers.idx - 25 AND numbers.idx - 1'
        '   AND numbers_b.idx BETWEEN numbers.idx - 25 AND numbers.idx - 1'
        ') IS NULL AND numbers.idx >= 25'
    )
    return cursor.fetchone()[0]


def part_two():
    cursor.execute(
        'SELECT ('
        '    SELECT MIN(numbers_sum.value) + MAX(numbers_sum.value)'
        '    FROM numbers AS numbers_sum'
        '    WHERE numbers_sum.idx BETWEEN numbers_start.idx AND numbers_end.idx'
        ') FROM (numbers AS numbers_start, numbers AS numbers_end)'
        'WHERE ('
        '    SELECT SUM(numbers_sum.value) FROM numbers AS numbers_sum'
        '    WHERE numbers_sum.idx BETWEEN numbers_start.idx AND numbers_end.idx'
        ') = ('
        '    SELECT value FROM numbers WHERE ('
        '        SELECT numbers_a.value'
        '        FROM (numbers AS numbers_a, numbers AS numbers_b)'
        '        WHERE numbers_a.value + numbers_b.value = numbers.value'
        '        AND numbers_a.value != numbers_b.value'
        '        AND numbers_a.idx BETWEEN numbers.idx - 25 AND numbers.idx - 1'
        '        AND numbers_b.idx BETWEEN numbers.idx - 25 AND numbers.idx - 1'
        '    ) IS NULL AND numbers.idx >= 25'
        ')'
    )
    return cursor.fetchone()[0]


db = sqlite3.connect(':memory:')
cursor = db.cursor()

store_input()
print(part_one())
print(part_two())
