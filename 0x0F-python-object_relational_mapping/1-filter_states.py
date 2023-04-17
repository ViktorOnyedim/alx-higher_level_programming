#!/usr/bin/python3
"""Lists all states with a name starting with N"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    host = "localhost"
    user, pwd, db = argv[1], argv[2], argv[3]

    """connect to the database"""
    db_connect = MySQLdb.connect(host=host, port=3306, user=user, passwd=pwd, db=db)

    """create cursor object to execute queries"""
    cur=db_connect.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()  
    for row in rows:
        print(rows);

    cur.close()
    db_connect.close()
