# This is a guess the number game

import random

secret = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secret:
        print('Your guess is too low.')
    elif guess > secret:
        print('Your guess is too high.')
    else:
        break  # This condidtion is the correct guess

if guess == secret:
    print('Good Job! You guessed my number in ' + str(guess) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret) + '.')

    
    
