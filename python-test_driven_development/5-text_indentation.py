#!/usr/bin/python3
"""
Module 5-text_indentation

function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result in text
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip() for line in result.split("\n")]

    print("\n".join(lines))
