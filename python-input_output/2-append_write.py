#!/usr/bin/python3
"""module to write a string at the end of a text file
"""


def append_write(filename="", text=""):
    """fonction that writes a string at the end of a text file
    and return the number of characters
    """
    with open(filename, "a", encoding="UTF8") as file:
        content = file.write(text)
        return (content)
