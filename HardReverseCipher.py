#!/usr/bin/env python
'''
This is a harder way to do stuff
'''
message = input("Enter the text to be encrypted here: ")
translated = ''
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1
print(translated)

