
fi = open("myfile.txt", "r")
#print(fi.read())
#print(type(fi))
txt = fi.read()
print(txt)
#print(type(txt))
fi.close()

with open("myfile.txt", "r") as f:
    txt2 = f.readlines()
    print(txt2)

print("end")
