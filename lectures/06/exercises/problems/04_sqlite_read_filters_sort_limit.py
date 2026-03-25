"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO 1: age >= 22
    cur.execute ("SELECT * FROM students WHERE age >= 22")
    age = cur.fetchall()
    for rows in age:
        print(rows)
    # TODO 2 + 3: order by age desc, limit 3
    cur.execute("SELECT * FROM students ORDER BY age DESC LIMIT 3")
    fur = cur.fetchall()
    for i in fur:
        print(i)
    # TODO 4: track='backend' and age < 23
    cur.execute('SELECT * FROM students WHERE track = "backend" AND age < 23')
    xr = cur.fetchall()
    for g in xr:
        print(g)
    conn.close()


if __name__ == "__main__":
    main()
