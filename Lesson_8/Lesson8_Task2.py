# Task 2
#
# Creating a dictionary.
#
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(country_name, capital):
    state = {}
    state[country_name] = capital
    print(state)

country_name = input('Please, enter ypur country: ')
capital = input('Please enter it\'s capital ')
make_country(country_name, capital)




