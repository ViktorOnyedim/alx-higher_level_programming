#!/usr/bin/python3
"""Lists all states with a name starting with N"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """connect to the database"""
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    """create cursor object to execute queries"""
    cur = db_connect.cursor()

    cur.execute("SELECT * FROM states
        WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(rows);

    cur.close()
    db_connect.close()
