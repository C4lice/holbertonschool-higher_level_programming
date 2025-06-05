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

    def to_json(self, attrs=None):
        '''
        fonction that return the dictionary representation of this class
        '''
        finaldict = {}
        if attrs:
            if all(not isinstance(type(attrs[0]), type(i)) for i in attrs):
                for i in attrs:
                    if i in self.__dict__:
                        finaldict[i] = self.__dict__[i]
                return finaldict
            else:
                return self.__dict__
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''
        fonction that replaces all attributes of the instance
        '''
        for i in json:
            self.__dict__[i] = json[i]
