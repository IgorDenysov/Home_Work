# Task 2
#
# The valid phone number program.
#
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

number = input('Please, enter phone number: ')

if number.isdigit():
    if len(number) == 10:
        print('ok')
else:
    print ('You entered wrong number, try again')