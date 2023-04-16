#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """connect to MySQL database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    """create cursor object to execute queries"""
    cur = db.cursor()

    query = "SELECT * FROM state ORDER BY states.id ASC"

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        for col in row:
            print(row)

    """Close cursor and database connection"""
    cur.close()
    db.close()
