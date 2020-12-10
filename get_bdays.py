import csv

with open("birthdays.csv", "r") as f:
    txt = csv.reader(f)
    print(txt)
    for row in txt:
        print(f"{row[0]} was born on {row[1]} {row[2]}")
