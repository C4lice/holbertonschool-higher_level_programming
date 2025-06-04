#!/usr/bin/python3

'''
This the module contain function for read a file
'''


def read_file(filename=""):

    """reads a UTF-8 text file and displays it on stdout"""

    with open(filename,"r", encoding='UTF-8') as file:
        print(file.read())
