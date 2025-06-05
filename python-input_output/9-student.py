#!/usr/bin/python3

'''
This module contain function
'''


class Student:
    '''
    class that represent students
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        fonction that return the dictionary representation of this class
        '''
        return self.__dict__
