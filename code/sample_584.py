import itertools
x = [1, 2, 3, 4, 5]
for v in itertools.accumulate(x):
    print(v)
