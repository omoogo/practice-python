# Title: Guessing Game One

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they 
# guessed too low, too high, or exactly right. (Hint: remember 
# to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when 
# the game ends, print this out.

import random

random_number = random.randint(1, 9)
number_of_guesses = 0

while True:
    guess = input('Guess the number please! (type exit to quit): ')

    if guess == 'exit':
        print('Number of guesses ' + str(number_of_guesses))
        break

    number_of_guesses = number_of_guesses + 1

    guess = int(guess)

    if guess == random_number:
        print('You guessed exactly right!')
    elif guess < random_number:
        print('Sorry! You guessed to low.')
    elif guess > random_number:
        print('Sorry! You guessed to high')



