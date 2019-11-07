#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

num = number

if number < 0:
    number = -number

LD = number % 10

if num < 0:
    LD = -LD

if LD > 5:
    print("Last digit of %d is %d and is greater than 5" % (num, LD))
elif LD == 0:
    print("Last digit of %d is %d and is 0" % (num, LD))
else:
    print("Last digit of %d is %d and is less than 6 and not 0" % (num, LD))
