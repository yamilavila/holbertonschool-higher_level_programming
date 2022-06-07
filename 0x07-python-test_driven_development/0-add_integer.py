#!/usr/bin/python3
"""
0.Integers addition
Test driven dev
Write a function that adds 2 integers
Returns the addition of a and b
"""

def add_integer(a, b=98):
    """a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
