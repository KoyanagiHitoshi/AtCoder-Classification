import itertools
x = "01"
for v in itertools.product(x, repeat=3):
    print("".join(v))
