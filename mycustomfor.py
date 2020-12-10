<<<<<<< HEAD
=======
#!/usr/bin/env python3

>>>>>>> 7c4dbaae982955f010c0be27eae510cbdfbe375b
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

<<<<<<< HEAD
for farm in farms:
    #print(farm)
    print(f"The {farm['name']} has: {farm['agriculture']}")
    print(f"The {farm['name']} has:")
    for ag in farm['agriculture']:
        print(f"    {ag}")


for num in range(1,11):
    print(num)
    for n in range(1,4):
        print(num + n)
=======
for x in farms:
    print("Information is : " + str(x))

for num, farm in enumerate(farms):
    print(f"Farm #{num} is called {farm['name']} and has:")
    for ag in farm['agriculture']:
        print(f"    {ag}")
>>>>>>> 7c4dbaae982955f010c0be27eae510cbdfbe375b
