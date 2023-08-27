import itertools
s = "1234"
for x, y, z in itertools.combinations_with_replacement(s, 3):
    print(x, y, z)
