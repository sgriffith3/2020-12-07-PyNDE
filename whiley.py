import time
import random

num = random.randint(1, 100)
print(f"{num},", end=" ", flush=True)
#
while num <= 75:
    num = random.randint(1, 100)
    print(f"{num},", end=" ", flush=True)
#    if num > 75:
#        break

#while True:
#    play_again = input("Do you want to play again? (y/N) ")
#    if play_again != "y":
#        print("Quitter!")
#        break
#    print("You have chosen to move on to the next level!")

# Start here
#while num <= 10:
#    print(num, end=" ", flush=True)
#    if num == 7:
#        break 
#    time.sleep(1)
#    num = num + 3
    # num += 1


# until a condition is met
