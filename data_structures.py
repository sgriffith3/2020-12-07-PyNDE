blank_list = []

myvar = ''
normal_list = ["item1", 23.4, myvar, ["cats", "dogs"], "final item"]
# index           0       1     2           3                4      
# normal_list[3] = ["cats", "dogs"]
# index               0        1
dogs = normal_list[3][1]

blank_dictionary = {}

# { key: value }

normal_dictionary = {"name": "Sam", "state": "PA", "shirt_color": "yellowy-plaid" }

bad_dictionary =  {"name": "Sam", "state": "PA", "shirt_color": "yellowy-plaid", 
                   "name": "Bob", "state": "TX", "shirt_color": "blue"}

bad_dictionary['name'] = "Steve"
print(bad_dictionary)

sam_info = {"name": "Sam", "state": "PA", "shirt_color": "yellowy-plaid"}

bob_info = {"name": "Bob", "state": "TX", "shirt_color": "blue"}

print(sam_info['state'])
print(bob_info['state'])

good_structure = [sam_info, bob_info]
print(good_structure)

blarf = "We are talking ABOUT strings"
print(blarf.upper())
print(blarf.lower())
print(blarf.title())

print("hi Jasmine!".upper())

# "Hi"
# "HI"
# "hi"
# "hI"

greeting = "Hi"
if greeting.upper() == "HI":
    print("You said 'HI'")
else:
    print("You did not say 'HI'")

