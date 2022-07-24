#!/usr/bin/env python3.7

number = int(input("How many values should we process: "))
for _ in range(1, number + 1):
    if _ % 5 == 0 and _ % 3 == 0:
        print("FizzBuzz")
    elif _ % 3 == 0:
        print("Fizz")
    elif _ % 5 == 0:
        print("Buzz")
    else:
        print(_)
    