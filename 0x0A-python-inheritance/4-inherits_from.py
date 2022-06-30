#!/usr/bin/python3
"""
Task 4; Only sub class of
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    directly or inderectly from the specified class, otherwise False
    """
    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
