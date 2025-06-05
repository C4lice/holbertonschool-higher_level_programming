#!/usr/bin/python3

'''
This module contain function
'''


class Student:
    '''
    class that represent students
    '''
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        '''
        fonction that return the dictionary representation of this class
        '''
        finaldict = {}
        itt = 0
        if attrs:
            for i in attrs:
                if (type(attrs[0]) is not type(attrs[itt])):
                    return self.__dict__
                itt += 1
                if i in self.__dict__:
                    finaldict[i] = self.__dict__[i]
            return finaldict
        else:
            return self.__dict__
