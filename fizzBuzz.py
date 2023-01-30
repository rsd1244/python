#!/bin/usr/bin/env python3

lower = int(input("Enter a number to start counting from: "))
upper = int(input("Enter a number to count up to: "))

total = upper - lower

div_30 = 0
div_5 = 0
div_3 = 0
div_2 = 0
div_3_2 = 0
div_none = 0

for number in range(lower, upper + 1):
    
    if number > 0:    

        if number % 30 == 0:
            print("Foo")
            div_30 += 1
        elif number % 5 == 0:
            print("Bar")
            div_5 += 1
        elif number % 3 == 0 and number % 2 == 0:
            print("FizzBuzz")
            div_3_2 += 1
        elif number % 3 == 0:
            print("Fizz")
            div_3 += 1
        elif number % 2 == 0:
            print("Buzz")
            div_2 += 1
        else:
            print("Bazz")
            div_none += 1

print("The total of numbers evaluated was " + str(total) +'.')
print("There were", div_30, "numbers that were divisible by 30.")
print("There were", div_5, "numbers that were divisible by 5.")
print("There were", div_3, "numbers that were divisible by 3.")
print("There were", div_2, "numbers that were divisible by 2.")
print("There were", div_3_2, "numbers that were divisible by both 3 and 2.")
print("There were", div_none, "numbers that didnt meet any of the requirments above.")


