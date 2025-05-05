#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit_nbr = abs(number) % 10
if number < 0:
    digit_nbr = -digit_nbr

if digit_nbr > 5:
    print(f"Last digit of {number} is {digit_nbr} and is greater than 5")
elif digit_nbr < 6 and digit_nbr != 0:
    print(f"Last digit of {number} is {digit_nbr} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {digit_nbr} and is 0")
