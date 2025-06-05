#!/usr/bin/python3

'''
This module contain function that append string in text
'''


import json


def load_from_json_file(filename):
    '''
    this function to append string in a file
    '''
    with open(filename, 'r', encoding='UTF-8') as fichier:
        return json.loads(fichier.read())
