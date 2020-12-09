#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    print("Information is : " + str(x))

for num, farm in enumerate(farms):
    print(f"Farm #{num} is called {farm['name']} and has:")
    for ag in farm['agriculture']:
        print(f"    {ag}")
