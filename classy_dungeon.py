#!/usr/bin/env python3

import random


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        starting_health = self.health
        if starting_health - damage > 0:
            self.health -= damage
        else:
            self.health = 0
            damage = starting_health


goblin = Enemy('goblin', 2, 1)
bat = Enemy('bat', 1, 2)


class Weapon:
    def __init__(self, armor, attack):
        self.armor = armor
        self.attack = attack
        self.health = 10

    def take_damage(self):
        damage = Enemy.attack
        self.damage -= Enemy.attack
        starting_health = self.armor
        if starting_health - damage > 0:
            self.armor -= damage
        else:
            self.health = 0
            damage = starting_health


sword_shield = Weapon(3, 1)
estoc_dagger = Weapon(2, 2)
magic_staff = Weapon(1, 3)


class Reward:
    def __init__(self, gold_pieces):
        self.gold_pieces = gold_pieces


small_chest = Reward(10)
large_chest = Reward(30)


def room_encounter():
    encounter = random.randint(1, 5)
    if encounter == 1:
        print("You see a goblin.")
        return ("foe", goblin)
    elif encounter == 2:
        print("You see a bat.")
        return ("foe", bat)
    elif encounter == 3:
        print("You see a small chest.")
        return ("reward", small_chest)
    elif encounter ==4:
        print("You see a large chest.")
        return ("reward", large_chest)
    else:
        print("You see nothing.")
    return


def combat(you, enemy):
    while (you.health > 0) and (enemy.health > 0):
        print(f"Your health is {you.health}.")
        print(f"{enemy.name}'s health is {enemy.health}.")
        enemy.take_damage(you.attack)
        print(f"Your health is {you.health}.")
        print(f"{enemy.name}'s health is {enemy.health}.")
        if enemy.health <= 0:
            print(f"{enemy.name} has died.")
            break
        you.health -= enemy.attack
        print(f"Your health is {you.health}.")
        print(f"{enemy.name}'s health is {enemy.health}.")
        if you.health <= 0:
            print("You have died.")
            break




def main():

    dung_entry_loop = ()
    while dung_entry_loop == ():
        print("Do you want to enter the dungeon? Yes(y) or No(n).")
        dung_entry = input()
        if dung_entry == "y":
            for x in range(0, 100):
                print("What is your starting equipment?")
                equip = input("1 = sword and shield, 2 = estoc and dagger, and 3 = magic staff")
                if equip == 1:
                    print("You have equipted the sword and shield.")
                    spelunker = sword_shield
                    break
                elif equip == 2:
                    print("You have equipted the estoc and dagger.")
                    spelunker = estoc_dagger
                    break
                elif equip == 3:
                    print("You have equipted the magic staff.")
                    spelunker = magic_staff
                    break
                else:
                    print("That is not a valid response, try again.")
                    continue
            rooms = random.randint(0, 3) + 3
            room_num = 1
            while rooms != 0:
                print(f"You have entered room {room_num}.")
                room_experience, item = room_encounter()
                if room_experience == "foe":
                    combat(spelunker, item) ## run combat function
                elif room_experience == "reward":
                    # reward() ## run reward function
                    pass
                room = input(f"Do you want to continue? Yes(y) or No(n).")
                if room == "y":
                    rooms -= 1
                    room_num += 1
                elif room == "n":
                    print("You have exited the dungeon.")
                    quit()
                else:
                    print("That is not a valid response, try again.")
            print("You have reached the end of the dungeon. Thanks for playing!")
            break
        elif dung_entry == "n":
            print("You did not enter the dungeon.")
            quit()
        else:
            print("That is not a valid response, try again.")


main()
