# Task 3
#
# Using python as a calculator.
#
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
#
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division


first_variable = float(input('Enter first number: '))
second_variable = float(input('Enter second number: '))
add = first_variable + second_variable
sub = first_variable - second_variable
division = first_variable / second_variable
multiplication = first_variable * second_variable
exponent = first_variable ** second_variable
modulus_first = abs(first_variable)
modulus_second = abs(second_variable)
floor_division = first_variable // second_variable
str = " of these numbers is: "
print('Sum', str, add)
print('Subtraction', str, sub)
print('Division', str, division)
print('Multiplication', str, multiplication)
print('Exponent', str, exponent)
print('Modulus', str, modulus_first, ' and ', modulus_second)
print('Floor division', str, floor_division)
