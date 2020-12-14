#!/usr/bin/env python3

# program that returns letter grade after numeric score entered

# python thinks a string is coming unless you wrap this in a float.
numscore = float(input("Please enter your numeric score: "))

if numscore > 100 or numscore < 0:
    print("That is an invalid score!")
elif numscore >= 90:
    print("Awesome! you made an A!")
elif numscore >= 80:
    print("Not bad! You made a B.")
elif numscore >= 70:
    print("Is mediocre your middle name? You made a C.")
elif numscore >= 60:
    print("You need to study a LOT more. You made a D.")
else:
    print("Repeat after me. 'Would you like fries with that?' You got an F.")

# Another one for fun.
ip = input("Please enter an IPv4 address: ")
octets = len(ip.split("."))
if octets == 4:
    print("This appears to be a valid IP address.")
elif octets > 4:
    print("You have too many octets for this to be valid.")
else:
    print("you have too few octets for this to be valid.")