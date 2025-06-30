#!/usr/bin/python3
"""
    function used to connect to
    and display data from a database
"""
import MySQLdb
import sqlalchemy
import sys


def mysqlconnect():
    """
    function that connects and displays the
    status and their identifier from the database
    """
    db_connection = MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cirsort = db_connection.cursor()
    cirsort.execute("SELECT * from states ORDER BY states.id ASC;")
    listed = cirsort.fetchall()
    for element in listed:
        print(element)
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
