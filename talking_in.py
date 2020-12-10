nums = [1, 2, 3, 4, 5, 6, 7]

# in
# not in




x = 3
if x not in nums:
    print("no!")
else:
    print("yes!")


banned_words = ["meany-face", "idiot", "dunce", ["moron", "idiot", "nice"]]
mywords = ["moron", "idiot", "nice"]
for word in mywords:
    if word not in banned_words:
        print(word)
    else:
        print("Santa is putting you on the naughty list for saying that!")


txt = "Santa is coming!"
if "a" in txt:
    print("You better watch out")
else:
    print("coal")

