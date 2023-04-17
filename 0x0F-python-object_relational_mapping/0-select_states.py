#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """connect to MySQL database"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    """create cursor object to execute queries"""
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    """Close cursor and database connection"""
    cur.close()
    db.close()
