# Task 2
#
# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers


import random

list1 = list()
list2 = list()
i = 0

while i < 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    i += 1

set1 = set(list1)
set2 = set(list2)

result_list = list(set1.intersection(set2))

print(set1, set2)
print(result_list)

