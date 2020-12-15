

try:
    calc1 = int(input("Number 1: "))
    calc2 = input("Number 2: ")
    result = 3.14 + calc2 * calc1
    print(result)
except ValueError:
    print("There was a ValueError in your code")
except TypeError:
    print("TypeError Here!")


