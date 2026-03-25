"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT COUNT(*) FROM students
    cur.execute("SELECT COUNT(*) FROM students")
    huh = cur.fetchone()
    print(huh)
    # TODO: SELECT AVG(age) FROM students
    cur.execute("SELECT AVG(age) FROM students")
    guh = cur.fetchone()
    print(guh)
    # TODO: SELECT MIN(age), MAX(age) FROM students
    cur.execute("SELECT MIN(age), MAX(age) FROM students")
    puh = cur.fetchone()
    print(puh)
    # TODO: SELECT track, COUNT(*) FROM students GROUP BY track
    cur.execute("SELECT track, COUNT(*) FROM students GROUP BY track")
    bruh = cur.fetchone()
    print(bruh)
    conn.close()


if __name__ == "__main__":
    main()
