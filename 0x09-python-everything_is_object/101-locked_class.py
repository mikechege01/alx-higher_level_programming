#!/usr/bin/python3
# Task 30
"""A class LockedClass with no class or object attribute"""


class LockedClass:
    """
    class LockedClass definition
    """
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("Cannot create new attribute '{}'".format(name))