import itertools
X = "abc"
Y = range(1, 4)
for x, y in itertools.product(X, Y):
    print(x, y)
