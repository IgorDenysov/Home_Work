# Task 1
#
# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers

import random

list_of_numbers = list()

maximum = 0
count = 0
i = 0

while i < 10:
    x = random.randint(0, 10)
    list_of_numbers.append(x)
    i += 1

for count in range(len(list_of_numbers)):
    if list_of_numbers[count] > maximum:
        maximum = list_of_numbers[count]
        count += 1

print(maximum)
