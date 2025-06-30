#!/usr/bin/python3
"""
    function that connect and display the
    state that have a N in first place int heir name
    and their id from the db

"""
import MySQLdb
import sys


def mysqlconnect():
    """
    function that links and displays
    the state that has an N in the first place in its name
    and their identifier in the database
    """
    db_connection = MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cirsort = db_connection.cursor()
    cirsort.execute("""SELECT * from states
        WHERE BINARY name = '{}'
        ORDER BY states.id ASC;""".format(sys.argv[4]))
    listed = cirsort.fetchall()
    for element in listed:
        print(element)
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
