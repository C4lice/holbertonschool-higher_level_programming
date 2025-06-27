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
    cirsort.execute("""SELECT cities.id, cities.name, states.name from states
        INNER JOIN cities ON states.id = cities.state_id
        ORDER BY cities.id ASC;""")
    listed = cirsort.fetchall()
    for element in listed:
        print(element)
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
