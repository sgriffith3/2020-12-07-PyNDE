#!/usr/bin/env python3
## create file object in "r"ead mode
#filename = input("What file are you looking to read? ")
with open(input("File name? "), "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
## file was just auto closed (no more indenting)

## display list with no "\n"
print(configlist)
print(len(configlist))
