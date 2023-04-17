#!/usr/bin/python3
"""
Takes in arguments and displays all values in the 'states' table of
'hbtn_0e_0_usa' where 'name' matches the argument
and is safe from MySQL injections
"""
import MySQLdb
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 5:
        exit(1)

    """Establish a database connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    """Create cursor object"""
    cur = db.cursor()
    """execute query"""
    cur.execute("SELECT * FROM states WHERE name \
        LIKE %s ORDER BY states.id ASC", (argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
