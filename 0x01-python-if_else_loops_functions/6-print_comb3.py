#!/usr/bin/python3

for i in range(0, 100):
    j = i // 10
    k = i % 10

    if j < k and i != 89:
        print("{:.0f}{:.0f}, ".format((i // 10), (i % 10)), end='')
    if i == 89:
        print("89")
