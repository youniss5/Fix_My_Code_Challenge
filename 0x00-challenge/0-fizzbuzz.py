#!/usr/bin/python3
""" code for fizz buzz """
import sys


def fizzbuzz(x):
    """ fizz buzz function"""
    if x < 1:
        return

    tm_res = []
    for i in range(1, x + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tm_res.append("FizzBuzz")
        elif (i % 3) == 0:
            tm_res.append("Fizz")
        elif (i % 5) == 0:
            tm_res.append("Buzz")
        else:
            tm_res.append(str(i))
    print(" ".join(tm_res))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
