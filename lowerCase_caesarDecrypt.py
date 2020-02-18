
#!/usr/bin/env/ python3
code = input("Enter the cipher text: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in code:
    ordValue = ord(ch)
    plainValue = ordValue - distance
    if plainValue < ord('a'):
        plainValue = ord('z') - (distance - (ord('a') - ordValue - 1))
    plainText += chr(plainValue)
print(plainText)

