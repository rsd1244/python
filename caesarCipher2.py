'''

Program: caesarCipher.py
Author: Ritchie Deel
Purpose: Encrypt or Decrypt a plain text string by shifting the string indexes based on a key length input by the user.

'''


import string    # Import the string library to generate our character list


# Prompt the user for a plain text string to be encrypted.
message = input("Enter the message to be encrypted here: ")


# Prompt the user for a key size. Verify that is is a int type.
while True:
    try:
        key = int(input("Enter the key here: "))
        break
    except ValueError as error:
        print(error)
        print("Key must be an integer. Please try again.")

# Set the mode to either encrypt or decrypt
mode = input("Enter the mode - [encrypt or decrypt]: ")

# Sets our character set
SYMBOLS = string.ascii_letters + string.digits + string.punctuation + " "

# Will store our translated message
translated = ''

for symbol in message:    # Loop to step through each symbol in the message.
    if symbol in SYMBOLS: # Checks to see if the symbol is in our character set
        symbolIndex = SYMBOLS.find(symbol)  # Find the index of the symbol in our character set.

        # Shifts the symbol left or right based on the mode and key size
        if mode in ['encrypt', 'Encrypt', 'ENCRYPT', 'e', 'E']:
            translatedIndex = symbolIndex + key
        elif mode in ['decrypt', 'Decrypt', 'DECRYPT', 'd', 'D']:
            translatedIndex = symbolIndex - key

            # Handle wrap around if necessary
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        # Add each translated symbol to the translated variable.
        translated += SYMBOLS[translatedIndex]
    else:
        #If the symbol is not in the character set, add the symbol to the translated message.
        translated += symbol

#Print the translated message.
print(translated)
