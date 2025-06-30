#!/usr/bin/python3
"""
module with one function used to connect
and display certain data from db
"""
import MySQLdb
import sys


def mysqlconnect():
    """
    function that connect and display the
    state that have a N in first place int heir name
    and their id from the db
    """
    db_connection = MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cirsort = db_connection.cursor()
    if "'" not in sys.argv[4]:
        cirsort.execute("""SELECT cities.id, cities.name from cities
            LEFT JOIN states ON cities.state_id = states.id
            WHERE BINARY states.name = '{}'
            ORDER BY cities.id ASC;""".format(sys.argv[4]))
        listed = cirsort.fetchall()
        for element in range(len(listed)):
            print(listed[element][1], end='')
            if element != len(listed) - 1:
                print(', ', end='')
        print('')
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
