#!/usr/bin/python3
"""
defines a fonction that read text file
"""


def read_file(filename=""):
    """
    open read and print the contant of a file
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(content, end="")
