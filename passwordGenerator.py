import random

password_length = int(input("Enter the length of requested password: "))

chars = "ABCDEFGHIJKLMNOPQRSTUVQRSYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?><+="

password = ""

for c in range(password_length):
    password += random.choice(chars)
print(password)
