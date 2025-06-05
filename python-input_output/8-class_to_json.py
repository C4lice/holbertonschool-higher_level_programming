#!/usr/bin/python3

'''
This module contain function
'''


def class_to_json(obj):
    '''
    returns the dictionary description with a
    simple data structure
    '''
    return obj.__dict__
