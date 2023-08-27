x = [1, 2, 3, 4, 5, 6]
for a, b in zip(*[iter(x)]*2):
    print(a, b)
