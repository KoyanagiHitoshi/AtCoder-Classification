import itertools
x = "ab"
y = "12"
for v in itertools.product(x, y, repeat=2):
    print(v)
