#!/usr/bin/python3
for c in range(0, 89):
        if (c // 10 != c % 10) and (c // 10 < c % 10):
            print("{:02d}, ".format(c), end="")
c += 1
print("{}".format(c))
