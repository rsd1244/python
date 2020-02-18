bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * pow(2, exponent)
    exponent = exponent -1
print("The integer value is", decimal)

