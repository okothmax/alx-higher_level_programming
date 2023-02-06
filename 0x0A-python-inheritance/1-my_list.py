#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """extended version of list
    """
    def print_sorted(self):
        """prints the list in ascending order
        """
        copy = self[:]
        copy.sort()
        print(copy)