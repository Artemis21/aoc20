import sqlite3


def get_input():
    print('Please enter the puzzle input:')
    inp = []
    y = 0
    while (line := input('... ')) != 'EOF':
        inp.append(line)
        y += 1
    return inp


def store_input():
    cursor.execute('CREATE TABLE lines (n INTEGER, line VARCHAR, start INTEGER);')
    cursor.executemany(
        'INSERT INTO lines (n, line) VALUES (?, ?);', enumerate(get_input())
    )
    cursor.execute('UPDATE lines SET start = 0 WHERE n = 0;')
    cursor.execute('UPDATE lines SET start = n WHERE line = "";')
    cursor.execute(
        'UPDATE lines SET start = ( '
        '    SELECT search_lines.start FROM lines AS search_lines WHERE '
        '    search_lines.start IS NOT NULL AND search_lines.start <= lines.n '
        '    ORDER BY search_lines.start DESC LIMIT 1 '
        ');'
    )
    data_query = (
        'SELECT '
        '    CASE WHEN INSTR(line, "byr:") = 0 THEN "" '
        '    ELSE SUBSTR('
        '        line, '
        '        INSTR(line, "byr:") + 4, '
        '        INSTR(SUBSTR(line || " ", INSTR(line, "byr:") + 4), " ") - 1'
        '    ) END byr, '
        '    CASE WHEN INSTR(line, "iyr:") = 0 THEN "" '
        '    ELSE SUBSTR('
        '        line, '
        '        INSTR(line, "iyr:") + 4, '
        '        INSTR(SUBSTR(line || " ", INSTR(line, "iyr:") + 4), " ") - 1'
        '    ) END iyr, '
        '    CASE WHEN INSTR(line, "eyr:") = 0 THEN "" '
        '    ELSE SUBSTR('
        '        line, '
        '        INSTR(line, "eyr:") + 4, '
        '        INSTR(SUBSTR(line || " ", INSTR(line, "eyr:") + 4), " ") - 1'
        '    ) END eyr, '
        '    CASE WHEN INSTR(line, "hgt:") = 0 THEN "" '
        '    ELSE SUBSTR('
        '        line, '
        '        INSTR(line, "hgt:") + 4, '
        '        INSTR(SUBSTR(line || " ", INSTR(line, "hgt:") + 4), " ") - 1'
        '    ) END hgt, '
        '    CASE WHEN INSTR(line, "hcl:") = 0 THEN "" '
        '    ELSE SUBSTR('
        '        line, '
        '        INSTR(line, "hcl:") + 4, '
        '        INSTR(SUBSTR(line || " ", INSTR(line, "hcl:") + 4), " ") - 1'
        '    ) END hcl, '
        '    CASE WHEN INSTR(line, "ecl:") = 0 THEN "" '
        '    ELSE SUBSTR('
        '        line, '
        '        INSTR(line, "ecl:") + 4, '
        '        INSTR(SUBSTR(line || " ", INSTR(line, "ecl:") + 4), " ") - 1'
        '    ) END ecl, '
        '    CASE WHEN INSTR(line, "pid:") = 0 THEN "" '
        '    ELSE SUBSTR('
        '        line, '
        '        INSTR(line, "pid:") + 4, '
        '        INSTR(SUBSTR(line || " ", INSTR(line, "pid:") + 4), " ") - 1'
        '    ) END pid '
        'FROM '
        '    (SELECT GROUP_CONCAT(line, " ") line FROM lines GROUP BY start)'
    )
    return data_query


def part_one(data_query):
    cursor.execute(
        f'SELECT COUNT(pid) FROM ({data_query}) WHERE '
        'byr != "" AND iyr != "" AND eyr != "" AND hgt != "" AND hcl != "" '
        'AND ecl != "" AND pid != "";'
    )
    return cursor.fetchone()[0]


def part_two(data_query):
    cursor.execute(
        f'SELECT COUNT(pid) FROM ({data_query}) WHERE '
        'LENGTH(byr) = 4 AND CAST(byr AS INTEGER) BETWEEN 1920 AND 2002 '
        'AND LENGTH(iyr) = 4 AND CAST(iyr AS INTEGER) BETWEEN 2010 AND 2020 '
        'AND LENGTH(eyr) = 4 AND CAST(eyr AS INTEGER) BETWEEN 2020 AND 2030 '
        'AND ( '
        '    ('
        '        hgt LIKE "%cm" '
        '        AND CAST(RTRIM(hgt, "cm") AS INTEGER) BETWEEN 150 AND 193 '
        '    ) OR ( '
        '        hgt like "%in" '
        '        AND CAST(RTRIM(hgt, "in") AS INTEGER) BETWEEN 59 AND 76 '
        '    )'
        ') '
        'AND LENGTH(hcl) = 7 AND hcl LIKE "#%" '
        'AND (UNICODE(SUBSTR(hcl, 2)) BETWEEN 48 AND 57 OR UNICODE(SUBSTR(hcl, 2)) BETWEEN 97 AND 102) '
        'AND (UNICODE(SUBSTR(hcl, 3)) BETWEEN 48 AND 57 OR UNICODE(SUBSTR(hcl, 3)) BETWEEN 97 AND 102) '
        'AND (UNICODE(SUBSTR(hcl, 4)) BETWEEN 48 AND 57 OR UNICODE(SUBSTR(hcl, 4)) BETWEEN 97 AND 102) '
        'AND (UNICODE(SUBSTR(hcl, 5)) BETWEEN 48 AND 57 OR UNICODE(SUBSTR(hcl, 5)) BETWEEN 97 AND 102) '
        'AND (UNICODE(SUBSTR(hcl, 6)) BETWEEN 48 AND 57 OR UNICODE(SUBSTR(hcl, 6)) BETWEEN 97 AND 102) '
        'AND (UNICODE(SUBSTR(hcl, 7)) BETWEEN 48 AND 57 OR UNICODE(SUBSTR(hcl, 7)) BETWEEN 97 AND 102) '
        'AND ( '
        '    ecl = "amb" OR ecl = "blu" OR ecl = "brn" OR ecl = "gry" '
        '    OR ecl = "grn" OR ecl = "hzl" OR ecl = "oth" '
        ') '
        'AND LENGTH(pid) = 9;'
    )
    return cursor.fetchone()[0]


db = sqlite3.connect(':memory:')
cursor = db.cursor()

data = store_input()
print(part_one(data))
print(part_two(data))
