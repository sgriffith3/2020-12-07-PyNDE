#!/usr/bin/env python3
#
# First Function Challenge!
#
# Create 2 functions, each one doing the following:
#
# 1. Taking in a name as a parameter, and printing out the phrase "Hello <name>"


def greeting(name):
    print("Hello {name}")
    print("Hello " + "name")
    print("Hello " + name)
    print("Hello {}".format(name))
    print(f"Hello {name}!")

greeting('bob')
greeting('steve')

while True:
    nam = input("Who is there? ")
    if nam.lower() == "quit":
        break
    greeting(nam)

# 2. Taking in a number as a parameter, printing out that number * 11, and returning that value
def times_11(num):
    product = num * 11
    print(product)
    return product


greeting(times_11(11))

my_num = int(input("What number should be multiplied by 11? "))
print(my_num)
times_11(my_num)



