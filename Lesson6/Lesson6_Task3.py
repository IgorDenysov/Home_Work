# Task 3
#
# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100, then find all integers from the list
# that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally,
# print the list.
#
# Constraint: use only while loop for iteration


list_by_7 = list()

count = 0
i = 0

while count in range(100):
    if ((count + 1) % 7) == 0:
        element = count + 1
        list_by_7.append(element)
    count += 1

while i in range(len(list_by_7)):
    if (list_by_7[i] % 5) == 0:
        list_by_7.remove(list_by_7[i])
    else:
        pass
    i += 1

print(list_by_7)