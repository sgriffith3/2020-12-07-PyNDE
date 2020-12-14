#!/usr/bin/env python3

rooms = ["living", "dining", "bath"]
bedrooms = ["master", "kid1", "kid2", "guest"]

rooms.insert(1, bedrooms)
print(rooms)

# rooms = ['living', ['master', 'kid1', 'kid2', 'guest'], 'dining', 'bath']
# index       0                        1                      2        3
# rooms[1] = ['master', 'kid1', 'kid2', 'guest']
# index          0         1       2       3

print(rooms[1][3])


