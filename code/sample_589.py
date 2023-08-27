import itertools
x = [5, 3, 4, 1, 2]
for v in itertools.accumulate(x, func=min):
    print(v)
