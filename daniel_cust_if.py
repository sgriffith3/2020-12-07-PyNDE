#!/usr/bin/env python3
import random
i = random.randint(1, 20)
print(f"Your die shows a {i}")
if i == 20:
    print("You rolled a critical!")
elif i >= 15:
    print("You hit your target.")
elif i >= 10:
    print("You missed your target.")
elif i >= 5:
    print("You dropped your weapon.")
elif i >= 2:
    print("You have wounded yourself.")
elif i == 1:
    print("You have slain yourself.")
else:
    print("This error should never appear.  Value of i is " + str(i))

