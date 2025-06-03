#!/usr/bin/python3


def read_file(filename=""):
    """reads a UTF-8 text file and displays it on stdout"""
    with open(filename,"r", encoding='utf-8') as my_file:
        print(my_file.read(), end="")
