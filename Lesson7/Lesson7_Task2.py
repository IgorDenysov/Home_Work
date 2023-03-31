# Task 2
#
# Input data:
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# Compute the total price of the stock where the total price is the sum of the price
# of an item multiplied by the quantity of this exact item.


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_value = {}

for count in stock:
    total_value[count] = stock[count] * prices[count]

total = sum(total_value[i] for i in total_value)

print("Value of different items:", total_value)
print("Total value: ", total)