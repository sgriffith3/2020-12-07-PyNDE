#!/usr/bin/env python3
import random

class Truck:
    def __init__(self, color="blue", passengers=2, bed_size=5):
        self.color = color
        self.passengers = passengers
        self.bed_size = bed_size
        self.position = 0
        self.health = 100

    def move_forward(self, spaces):
        self.position += spaces
        print(f"Your Truck is at position: {self.position}")


    def fender_bender(self):
        damage = random.randint(15, 45)
        starting_health = self.health
        if starting_health - damage > 0:
            self.health -= damage
        else:
            self.health = 0
            damage = starting_health
        print(f"Your truck received {damage} damage. You are at {self.health} health")


my_chevy = Truck("red", 3, 8)
#print("My Chevy is:")
#print(my_chevy.color)
#print(my_chevy.passengers)
#print(my_chevy.bed_size)
print(my_chevy.position)
#print(my_chevy.health)
my_chevy.move_forward(3)

my_chevy.fender_bender()
my_chevy.fender_bender()
my_chevy.fender_bender()
my_chevy.fender_bender()
my_chevy.fender_bender()
my_chevy.fender_bender()






#my_ford = Truck(passengers=6, bed_size=6)
#print(my_ford.color)
#print(my_ford.passengers)
#print(my_ford.bed_size)




# color: red
# passengers: 3
# bed-size: 8

#txt1 = "This is talking about classes"
#txt2 = "So is this!"

#print(type(txt1))
#print(type(txt2))
