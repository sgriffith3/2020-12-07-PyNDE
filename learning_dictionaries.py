#!/usr/bin/env python3

# key: value
# basic_dictionary = {"key": "value"}

# random_word = {"aglet": "the tip of a shoelace"}
# print(random_word)
# print(random_word["aglet"])

# myform = {"name": "Sam", "State": "PA"}
# print(myform)
# print(f"My name is {myform['name']} and I live in {myform['State']}")

my_car = {"year": 2011, "color": "white", "style": "minivan"}
print(type(my_car))
print(my_car)
print(f"I drive a {my_car['year']} {my_car['color']} {my_car['style']}")

print(my_car.get('year'))
print(my_car.get("drivetrain"))

print(my_car.keys())
print(my_car.values())

print(my_car.items())


#mystr = "This is a pretty 'cool' string"

