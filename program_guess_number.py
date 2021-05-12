# This is a guess the number game.

import random   # requires a random number, import the random module

print('Hello. What is your name?') # greet the player, request import   
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20) #creates variable stored with the number

for guessesTaken in range(1, 7): # loop variable guessesTaken in range between but not including 1 to 7 so six guesses
    print('Take a guess.')
    guess = int(input())    #inputs are read as string, even if the value is numerical. to execute math statements on the input it needs to convert to int type.

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #this condition is for the correct guess!

if guess == secretNumber:
    print('Good Job, ' + name + '! You guessed my nubmer in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
