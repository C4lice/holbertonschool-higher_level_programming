#!/usr/bin/python3

'''
This module contain function that append string in text
'''


def append_write(filename="", text=""):
    '''
    this function to append string in a file
    '''
    with open(filename, 'a', encoding='UTF-8') as fichier:
        return fichier.write(text)
