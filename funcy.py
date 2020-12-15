"""
This is an example of a basic function.
"""

def add_111(any_number):
    """
    This function adds 111 to any_number
    """
    response = any_number + 111
    print(f"Your number is: {response}")
    return response


add_111(55)
add_111(5)
add_111(89)
add_111(3.14)
print(add_111(42))
x = add_111(add_111(1))
print(x, "coolio")
# def print(*objects, sep=" ", end="\n" ...):

# print("something")
