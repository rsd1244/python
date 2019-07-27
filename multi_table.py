#!/usr/bin/env python3

#Python table to print the multiplication table of a give number

n = int(input('Enter a number: '))

for i in range(1,101):
        print(n, 'x', i, '=', n*i)
