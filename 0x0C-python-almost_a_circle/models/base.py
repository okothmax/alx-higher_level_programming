#!/bin/bash/python3
"""
creating the Base class
"""

class Base:
    '''
    private class attributes
    
    nb_objects'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            