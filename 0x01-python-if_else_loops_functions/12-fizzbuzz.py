#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0 and i != 99:
            print("FizzBuzz ", end='')
        elif i % 5 == 0:
            print("Buzz ", end='')
        elif i % 3 == 0:
            print("Fizz ", end='')
        elif i == 99:
            print("Fizz Buzz")
        else:
            print("{} ".format(i), end='')
