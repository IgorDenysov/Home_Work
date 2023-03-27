# Task 1
#
# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and lets the user guess what number
# was generated. The result should be sent back to the user via a print statement.


import random

a = random.randint(1, 10)

while True:
    number = int(input('Guess a number: '))
    if number == a:
        print('You win!!!')
        continue
    else:
        print('You loose(((')
        continue