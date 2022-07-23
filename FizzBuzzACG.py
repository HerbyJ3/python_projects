#!/usr/bin/env python3.7

number = int(input("Enter an integer: "))
if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
    