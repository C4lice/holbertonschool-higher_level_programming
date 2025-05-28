#!/usr/bin/python3
"""
module that create a square class
"""

class MyList(list):
    """
    create a class MyList
    """
    def print_sorted(self):
        """
        function print the list in ascending order
        """
        print_list = self.copy()
        print_list.sort()
        print(print_list)
