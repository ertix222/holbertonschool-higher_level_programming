#!/usr/bin/python3
def uppercase(str):
    for a in str:
        value = ord(a)
        if (ord(a) in range(97, 123)):
            value = value-32
        print("{}".format(chr(value)), end="")
    print("")
