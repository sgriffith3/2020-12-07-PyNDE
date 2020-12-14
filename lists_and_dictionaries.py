#!/usr/bin/env python3

cars = [
    {"type": "ford", "model": "t"},
    {"type": "chevy", "model": "corvette"}
    ]

for car in cars:
    print(f"Car # {cars.index(car) + 1} is a {car['type']} and it's model is {car['model']}")

# for car in enumerate(cars):
#    print(car)
#    print(f"My car # is a {car[1]['type']} and it's model is {car[1]['model']}")

# (0, {'type': 'ford', 'model': 't'})
for ind, car in enumerate(cars):
    print(ind)
    print(car)
    print(f"My car # {ind + 1} is a {car['type']} and it's model is {car['model']}")
