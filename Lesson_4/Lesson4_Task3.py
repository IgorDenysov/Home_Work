# Task 3
#
# The math quiz program.
#
# Write a program that asks the answer for a mathematical expression, checks whether the user is right
# or wrong, and then responds with a message accordingly.

print('Mathematical quiz!!!')
number1 = int(input('Please, enter the first number: '))
number2 = int(input('Please, enter the second number: '))

product = number1 * number2
result = int(input('Please enter product: '))

if product == result:
    print('YOU WIN!!!')
else:
    print('YOU LOOSE(((')
