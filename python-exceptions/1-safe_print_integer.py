#!/usr/bin/python3
def safe_print_integer(value):
    if not isinstance(value, int):
        return False
    try:
        print("{:d}".format(value))
    except TypeError:
        pass
    return True
