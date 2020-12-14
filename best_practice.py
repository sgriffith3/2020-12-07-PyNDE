#!/usr/bin/env python3

"""
This script is intended to show best practice for script writing.

Author | Sam Griffith

License | MIT
"""

# Python Standard Library
import csv

# 3rd Party Packages - Also should be listed in the requirements.txt file
import requests


# GLOBAL VARS
DNS_SERVER = "8.8.8.8"


# Classes
class Kangaroo:
    pass


# Defining Functions
def add_22(num):
    """
    This function adds 22 to your number
    :param num: this should be an integer
    :return: value of num + 22
    """
    new_num = num + 22
    return new_num


def main():
    num = add_22(22)
    print(num)


if __name__ == "__main__":
    main()
