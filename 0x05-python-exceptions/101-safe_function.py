#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    reslt = None
    try:
        reslt = fct(*args)
    except:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
    return reslt
