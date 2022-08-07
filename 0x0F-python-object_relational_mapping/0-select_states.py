#!/usr/bin/python3
"""Task 0.Get all states"""

import sys
import MySQLdb

if __name__ == '__main__':
    database = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passw=argv[2], db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for states in rows:
        print(states)
