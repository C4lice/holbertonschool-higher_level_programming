#!/usr/bin/python3def safe_print_integer(value):
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
