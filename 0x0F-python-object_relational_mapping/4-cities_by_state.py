#!/usr/bin/python3
"""
Lists all 'cities' from the database 'hbtn_0e_4_usa'
Takes 3 arguments:
-> mysql username
-> mysql password
-> database name
"""
import MySQLdb
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 4:
        exit(1)

    """Establish database connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """Create cursor object"""
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
