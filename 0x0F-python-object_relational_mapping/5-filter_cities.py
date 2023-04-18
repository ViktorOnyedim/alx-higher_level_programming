#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 5:
        exit(1)

    """Establish database connection"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """Create cursor object"""
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()
