#!/usr/bin/python3
"""Task 1.Filter states"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    database = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")
    rows = cursor.fetchall()
    for states in rows:
        print(states)
    cursor.close()
    database.close()
