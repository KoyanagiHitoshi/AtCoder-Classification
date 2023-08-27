X = [2, 4, 5]
print("Even" if all(x % 2 == 0 for x in X) else "Odd")
