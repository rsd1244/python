

#!/usr/bin/env python
'''
This is a simple Ceaser Cipher that prompts the user for a string, key, and mode 
and then carries out encryption or decryption on the string.
Author: Ritchie Deel
'''
# The string to be encrypted/decrypted is input here:
message = input("Enter the message to be encrypted here: ")
# The encryption/decryption key:
key = int(input("Enter the encryption key: "))
# Whether the program will encrypt or decrypt the string:
mode = input('Enter the mode (encrypt or decrypt): ')
# Every possible symbol that is allowed to be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# Stores the encrypted/decrypted form of the message:
translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        # Perform encryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
       # Handle wrap-around, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol
# Output the translated string:
print(translated)

