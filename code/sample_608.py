import itertools
x = "123"
for v in itertools.product(x, repeat=2):
    print(v)
