#!/usr/bin/python3
"""
    function used to connect and
    display certain database data
"""
import MySQLdb
import sys


def mysqlconnect():
    """
    function that links and displays reports
    that have an N in the first place with their
    name and identifier in the database
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
        WHERE BINARY name LIKE 'N%'
        ORDER BY states.id ASC;""")
    listed = cirsort.fetchall()
    for element in listed:
        print(element)
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
