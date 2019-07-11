# simple guessing game using a while loop

import random

guessTaken = 0

print('Hello, what is your name?')
name = input()

number = random.randrange(1,11)
print("Well hello " + name + ". I am thinking of a number between 1 and 10. Can you guess the number?")
print('I will give you 5 guesses.')

while guessTaken < 5:
    print('Take a guess: ')
    guess = int(input())

    guessTaken = guessTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken)
    print('Boom! You got it! My number was ' + str(number) + '!')
    print('Good job ' + name + "! You guessed my number in " + guessTaken + " guesses!")

if guess != number:
    number = str(number)
    print('Uh Oh! You have run out of guesses. The number I was thinking of was ' + number + '.')
