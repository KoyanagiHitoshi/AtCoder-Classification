import itertools
X = "abc"
Y = ("AB", "CD")
Z = range(1, 3)
for x, y, z in itertools.product(X, Y, Z):
    print(x, y, z)
