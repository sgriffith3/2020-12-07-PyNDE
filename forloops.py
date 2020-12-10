# for <iterator> in <iterable>:
# for <item> in <iterable>:
#     do this code

# lists and strings are iterable objects
cats = ["fluffy", "snowball", "mr. snuffles", "tigger"]

# for each item in cats:
for shoe in cats:
    print("The cat's name is:")
    print(shoe.title())

print("The cats for loop is over")


#for num in nums:
#    plus_10 = num + 10
#    print(f"{num} + 10 = {plus_10}")
    #print(str(num) + " + " + "10 = " + str(plus_10)) 

nums = [11, 42, 78, 13, 42, 111, 56, 99]
for num in nums:
    print(f"You scored: {num}")
    if num < 0 or num > 100:
        print("That's impossible!")
    elif num >= 90:
        print("You rocked that! A!!!")
    elif num >= 80:
        print("You Better Be Better next time! (B)")
    elif num >= 70:
        print("C you later")
    elif num >= 60:
        print("D + unce = you")
    else:
        print("F ...")

