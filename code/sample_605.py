import itertools
x = ["a", "b", "c"]
y = ["1", "2", "3"]
for v in itertools.product(x, y):
    print(v)
