# Task 1
#
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.

from collections import Counter


sentence = input('Please, enter your sentence: ')

list_sentence = sentence.split()

result_dict = Counter(list_sentence)

print(result_dict)
