#!/usr/bin/python3
"""
defines a fonction that write a string to a text file
"""


def write_file(filename="", text=""):
    """
    open and write in a text file
    and returns number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        charac_written = f.write(text)
    return charac_written
