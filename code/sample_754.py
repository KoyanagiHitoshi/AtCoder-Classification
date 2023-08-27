import itertools
s = "12345"
for x, y, z in itertools.combinations(s, 3):
    print(x, y, z)
