numbers = range(1,10)
ranks = []
for num in numbers:
    if num == 1:
        ordinal = "st"
    elif num == 2:
        ordinal = "nd"
    elif num == 3:
        ordinal = "rd"
    elif num >= 4:
        ordinal = "th"
    ranks.append(f"{num}{ordinal}")
print(", ".join(ranks))
