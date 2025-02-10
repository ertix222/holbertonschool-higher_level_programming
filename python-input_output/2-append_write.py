#!/usr/bin/python3
"""
defines a fonction that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    write at the end of a file without erase
    or create if it doesn't exist
    """
    with open(filename, "a", encoding="utf-8") as f:
        app = f.write(text)
    return (app)
