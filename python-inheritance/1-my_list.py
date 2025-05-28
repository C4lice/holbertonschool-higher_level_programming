#!/usr/bin/python3
"""
module that create a square class
"""


class MyList(list):
    """
    create a class MyList
    """
    def print_sorted(self):
        print_list = self[:]
        print_list.sort()
        print(print_list)
