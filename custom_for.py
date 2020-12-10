farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

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
