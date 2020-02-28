#!/usr/bin/env python3
"""
Password Generator Test Script
By Ritchie Deel

This script will prompt the user for their password's length then it will ask for the complexities
of the password they want. It will then print that password. It also handles invalid user input.
"""

#import the random module.
import random
#import the string module.
import string
#get all of the uppercase ascii letters(A-Z) and set it to upper.
upper = string.ascii_uppercase
#get all of the lowercase ascii letters(a-z) and set it to lower.
lower = string.ascii_lowercase
#get all of the ascii digits 0-9 and set it to number.
number = string.digits
#get all of the punctuation characters,everything that's no already covered and printable.
punctuation = string.punctuation

#This is our input validation loop. 
#It always runs until they enter valid input.
while True:
    #try to get the input from them as an int. If it works we break from teh loop.
    try:
        password_length = int(input("Enter the length of requested password: "))
        break
    #otherwise we've got a value error. So we set it to the variable error so we can print it.
    except ValueError as error:
        #print their error.
        print(error)
        #also tell them to try again.
        print("Please try again.")

#initialize some variables.
charset=""
#
password=""

#prompt them for if they want uppercase letters.
use_upper = input("Use uppercase letters? Y or N: ")

#same for lowercase.
use_lower = input("Use lowercase letters? Y or N: ")

#same for the digits.
use_number = input("Use numbers? Y or N: ")

#same for punctuation.
use_punctuation = input("Use punctuation? Y or N: ")

"""see if their input is either Y or y.
Basically the in operator lets you see if some value is in a list or dict or tuple.
This let's me cover both uppercase and lowercase instances of Y just to make it easier on the user.
"""
if use_upper in ["Y","y"]:
    #if it is then we append uppercase letters to our character set.
    charset+=upper
    
if use_lower in ["Y","y"]:
    #same with lowercase.
    charset+=lower
if use_number in ["Y","y"]:
    #and the digits.
    charset+=number
    
if use_punctuation in ["Y","y"]:
    #and finally the punctuation.
    charset+=punctuation

#here I see if punctuation was changed. If all of the other if statements fail it's still gonna be blank.
#thus meaning they didn't enter _any_ valid information outside of the length of the target password.
if len(charset) == 0:
    #tell them that they didn't give us at least one valid choice.
    print("Please enter a valid choice. At least one option has to be chosen.")
    
#otherwise we're good to go.
else:
    #list comprehension version.
    #''.join(random.choice(charset) for x in range(password_length))
    
    #loop version.
    for x in range(password_length):
        password+=random.choice(charset)
    
    #finally print their generated password.
    print("Your generated password is")
    print(password)
