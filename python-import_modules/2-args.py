#!/usr/bin/python3

if __name__ == "__main__":
    import sys

if len(sys.argv) == 1:
    print("0 arguments.")

elif len(sys.argv) == 2:

    print("1 argument:")
    print("1: {}".format(sys.argv[1]))

else:

    arg_number = len(sys.argv) - 1
    print("{} arguments:".format(arg_number))

    for i in range(1, arg_number + 1):
        print("{}: {}".format(i, sys.argv[i]))
