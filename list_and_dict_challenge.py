#!/usr/bin/env python3
#
# List and Dictionary Challenge!
#
# Create a list of dog names (at least 3)
dogs = ["fido", "bingo", "spot"]

# Create another list of cat names (at least 3)
cats = ["fluffy", "snowball", "precious"]

print(dogs)

# Append the cats list onto the dogs list (so it is a single list)
dogs.append(cats)
print(dogs)

# Print out the first dog name from your single list
print(dogs[0])

# Print out the second cat name from your single list
# dogs = ['fido', 'bingo', 'spot', ['fluffy', 'snowball', 'precious']]
# index      0       1        2                   3
# dogs[3] = ['fluffy', 'snowball', 'precious']
# index         0           1           2
print(dogs[3][1])

# Create a dictionary with the keys "first_dog" and "second_cat".
# Use the appropriate values from your list as the values for the dictionary keys
catdog = {"first_dog": dogs[0], "second_cat": dogs[3][1]}

# Print out the dictionary
print(catdog)

# Print out the value of "first_dog" and "second_cat" from the dictionary
print(catdog['first_dog'], catdog['second_cat'])
