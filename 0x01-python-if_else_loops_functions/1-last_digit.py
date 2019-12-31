#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    n_number = -number
    LD = -1 * (n_number % 10)
else:
    LD = number % 10

print("Last digit of " + str(number) + " is " + str(LD), end=" ")
if LD > 5:
    print("and is greater than 5")
elif LD is 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
