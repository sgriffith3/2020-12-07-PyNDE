#!/usr/bin/env python3

message = 'Your game with be starting soon, '

#
avatar = input("Please select an Avatar. ")

#
if avatar == "Elf":
    message = message + 'setting up elf profile.'
elif avatar == "Warrior":
    message = message + 'setting up warrior profile.'
elif avatar == "Rogue":
    message = message + 'setting up rogue profile.'
else:
    message = message + 'you did not provide input. Timed out!'
print(message)


