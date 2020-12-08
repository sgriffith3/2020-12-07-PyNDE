#!/usr/bin/env python3

cats = ["garfield", "tigger", "mufasa"]
print(cats)

cats.append("simba")
print(cats)

cats.remove("garfield")
print(cats)

cats.reverse()
print(cats)

new_cat = ["nala", "scar"]
cats.extend(new_cat)
print(cats)

pets = [["dogs", "cats", "fish"], ["iguana", "tortoise", "llama"]]
# index            0                            1

print(pets[0])
# pets[0] = ['dogs', 'cats', 'fish']
# index        0        1       2
normal_pets = pets[0]
print(normal_pets[2])
print(pets[0][1])

print(pets[1])
# pets[1] = ['iguana', 'tortoise', 'llama']
# index          0          1         2
print(pets[1][2])
