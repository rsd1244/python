'''
passwordGen.py
Author: Ritchie Deel
This program prompts user for a password length as well as if they want uppercase, lowercase, numbers, and or
punctuation in their password.
'''

import random # Import random to generate random password
import string # Import string to generate upper, lower, numbers, and punctuation in passwords

upper = string.ascii_uppercase    # Stores all uppercase letters
lower = string.ascii_lowercase    # Stores all lowercase letters
numbers = string.digits           # Stores all digits 0-9
punctuation = string.punctuation  # Stores all punctuation chars

password = ''    # Used to store password
charset = ''     # Used to store charset to be passed to our random.choice()

# Check for password length. If not int, print error and ask for password length again.
while True:
    try:
        password_length = int(input("Enter the length of requested password: "))
        break
    except ValueError as error:
        print(error)
        print("Password length must be an integer, please try again.")

# Ask the user if they would like uppercase chars in their password
use_upper = input("Would you like uppercase characters in your password? [Y or N]: ")

# Ask the user if they would like lowercase chars in their password
use_lower = input("Would you like lowercase characters in your password? [Y or N]: ")

# Ask the user if they would like numbers chars in their password
use_numbers = input("Would you like numbers in your password? [Y or N]: ")

# Ask the user if they would like uppercase chars in their password
use_punctuation = input("Would you like punctuations in your password? [Y or N]: ")

# If user enters "y" or "Y" for use_uppercase letters, append upper to charset
if use_upper in ('Y', 'y'):
    charset += upper

# If user enters "y" or "Y" for use_lowercase letters, append lower to charset
if use_lower in ('Y', 'y'):
    charset += lower

# If user enters "y" or "Y" for use_numbers, append numbers to charset
if use_numbers in ('Y', 'y'):
    charset += numbers

# If user enters "y" or "Y" for use_punctuation, append punctuation to charset
if use_punctuation in ('Y', 'y'):
    charset += punctuation

"""" Handle error if user answered "N" to all the above.  If they did a password cannot be generated.
Tell them they must choose at least one of the selections and to try again if they did not choose at least one.
"""

if len(charset) == 0:
    print("Selections are empty, you must choose at least one upper, lower, number or punctuation.  Please try again.")

# Otherwise, we can generate the user a password based on their selections made previously in the program.
else:
    # list comprehension version.
    # ''.join(random.choice(charset) for x in range(password_length))

    # Here we loop through the length of the reqested password and append the password varible with a random choice of chars
    for x in range(password_length):
        password += random.choice(charset)

    # We then print the users generated password
    print("Here is your secure password: "+ password)
