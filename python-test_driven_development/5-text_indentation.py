#!/usr/bin/python3
"""
module used to indent a text depending on punctuation
"""


def text_indentation(text):
    """
    checks if it's a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = 0
    Poncts = ".?:"
    while a < len(text):
        if text[a] in Poncts:
            print(text[a])
            print()
            a += 1
            while a < len(text) and text[a] == " ":
                a += 1
        else:
            print(text[a], end="")
            a += 1
